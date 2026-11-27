"""
Analizador semantico de BabyDuck.

Se encarga de las TABLAS: directorio de funciones, tablas de variables y
memoria virtual. Sabe en que ambito (programa o funcion) se esta en cada
momento y reporta los errores semanticos.

Decisiones de diseno:
  - Una variable local o un parametro no puede llamarse igual que una global.
    Tambien se rechaza el nombre repetido dentro del mismo ambito.
  - Los errores se acumulan en self.errores y el analisis continua, para
    reportar todos los errores de una sola vez.
"""
from .directorio_funciones import DirectorioFunciones, Funcion
from .memoria_virtual import MemoriaVirtual
from .tabla_variables import TablaVariables


class AnalizadorSemantico:
    def __init__(self):
        self.memoria = MemoriaVirtual()
        self.directorio = None
        self.ambito = None          # Funcion en la que se esta (el programa o una funcion)
        self.errores = []

    def error(self, linea, mensaje):
        """Anota un error semantico; el analisis continua."""
        self.errores.append(f"línea {linea}: {mensaje}")

    # ------------------------------------------------------------------
    # Programa
    # ------------------------------------------------------------------
    def inicio_programa(self, nombre):
        """Crea el directorio; el programa es el primer ambito (el global)."""
        self.directorio = DirectorioFunciones(nombre, self.memoria)
        self.ambito = self.directorio.programa

    def inicio_main(self):
        """main tiene su propio espacio de temporales."""
        self.memoria.reiniciar_locales()

    def fin_programa(self):
        """Guarda cuanta memoria global y de main necesita el programa."""
        self.directorio.programa.tamano = {
            "global": self.memoria.tamano("global"),
            "local": self.memoria.tamano("local"),
            "temporal": self.memoria.tamano("temporal"),
        }

    # ------------------------------------------------------------------
    # Variables
    # ------------------------------------------------------------------
    def declarar_variables(self, nombres, tipo, linea):
        """Declaracion  'a, b, c : int;'  en el ambito actual."""
        for nombre in nombres:
            if not self.directorio.agregar_variable(self.ambito, nombre, tipo):
                if (
                    self.ambito is not self.directorio.programa
                    and self.directorio.global_.existe(nombre)
                ):
                    self.error(
                        linea,
                        f"variable local '{nombre}' no puede tener el mismo nombre que una global",
                    )
                else:
                    self.error(linea, f"variable '{nombre}' doblemente declarada")

    def buscar_variable(self, nombre, linea):
        """
        Busca una variable que se va a usar (en el ambito actual y luego en el global).

        Returns:
            dict {"tipo", "address"} o None (y reporta el error) si no existe.
        """
        info = self.directorio.buscar_variable(nombre, self.ambito)
        if info is None:
            self.error(linea, f"variable '{nombre}' no declarada")
        return info

    def usar_variable(self, nombre, linea):
        """Igual que buscar_variable, pero solo devuelve el tipo (o None)."""
        info = self.buscar_variable(nombre, linea)
        if info is None:
            return None
        return info["tipo"]

    # ------------------------------------------------------------------
    # Funciones
    # ------------------------------------------------------------------
    def inicio_funcion(self, nombre, retorno, linea):
        """
        Registra la funcion y la vuelve el ambito actual.

        Args:
            nombre (str): nombre de la funcion.
            retorno (str): "void", "int" o "float".
            linea (int): para reportar errores.
        """
        funcion = self.directorio.agregar_funcion(nombre, retorno)
        if funcion is None:
            self.error(linea, f"función '{nombre}' doblemente declarada")
            # Su cuerpo se analiza en una funcion desechable para no ensuciar el directorio
            funcion = Funcion(nombre, retorno)
            funcion.variables = TablaVariables(self.memoria, "local")

        # 1. Cada funcion empieza su propio espacio de locales y temporales
        self.memoria.reiniciar_locales()

        # 2. El valor de retorno se deja en una variable GLOBAL propia de la funcion:
        #    asi sobrevive cuando se destruye el registro de activacion al regresar.
        if funcion.regresa_valor():
            funcion.retorno_address = self.memoria.asignar_variable("global", retorno)

        self.ambito = funcion

    def agregar_parametro(self, nombre, tipo, linea):
        """Parametro  'n : int'  de la funcion actual (en orden)."""
        if not self.directorio.agregar_parametro(self.ambito, nombre, tipo):
            if self.directorio.global_.existe(nombre):
                self.error(
                    linea,
                    f"parámetro '{nombre}' no puede tener el mismo nombre que una variable global",
                )
            else:
                self.error(
                    linea,
                    f"parámetro '{nombre}' repetido en la función '{self.ambito.nombre}'",
                )

    def fin_funcion(self, linea):
        """Valida el return, guarda el tamano de la funcion y vuelve al ambito global."""
        funcion = self.ambito

        if funcion.regresa_valor() and not funcion.tiene_return:
            self.error(linea, f"la función '{funcion.nombre}' debe regresar un valor (falta return)")

        funcion.tamano = self.memoria.tamano_funcion()
        self.ambito = self.directorio.programa

    def llamar_funcion(self, nombre, linea):
        """
        Valida que la funcion que se llama exista.

        Returns:
            Funcion o None (y reporta el error) si no existe.
        """
        funcion = self.directorio.obtener_funcion(nombre)
        if funcion is None or nombre == self.directorio.nombre_programa:
            self.error(linea, f"función '{nombre}' no declarada")
            return None
        return funcion
