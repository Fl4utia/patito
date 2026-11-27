"""
Directorio de Funciones: registro de todas las funciones del programa.

Estructura:  diccionario  nombre -> Funcion

El programa mismo se registra como una entrada mas; su tabla de variables es
la tabla global.
"""
from .tabla_variables import TablaVariables


class Funcion:
    """Todo lo que el compilador y la maquina virtual necesitan saber de una funcion."""

    def __init__(self, nombre, retorno):
        self.nombre = nombre

        # "void", "int" o "float".  None para el programa principal.
        self.retorno = retorno

        # Lista ORDENADA de (nombre, tipo): el orden importa para validar las llamadas
        self.parametros = []

        # Tabla de variables propia (parametros + variables locales)
        self.variables = None

        # Numero del primer cuadruplo de la funcion (a donde salta GOSUB)
        self.inicio = None

        # Variable GLOBAL donde la funcion deja su valor de retorno (solo int/float)
        self.retorno_address = None

        # Se marca al encontrar un 'return' en el cuerpo
        self.tiene_return = False

        # Recursos que usa:  {"local": {tipo: n}, "temporal": {tipo: n}}
        # (el programa ademas guarda "global").  ERA lo usa para reservar memoria.
        self.tamano = None

    def regresa_valor(self):
        """True si la funcion regresa int o float."""
        return self.retorno in ("int", "float")


class DirectorioFunciones:
    def __init__(self, nombre_programa, memoria=None):
        self.nombre_programa = nombre_programa
        self.memoria = memoria
        self.funciones = {}

        # El programa se registra como la primera "funcion"; su tabla es la global
        programa = Funcion(nombre_programa, None)
        programa.variables = TablaVariables(memoria, "global")
        self.funciones[nombre_programa] = programa

    @property
    def programa(self):
        """Entrada del programa principal."""
        return self.funciones[self.nombre_programa]

    @property
    def global_(self):
        """Tabla de variables globales (la del programa)."""
        return self.programa.variables

    def existe_funcion(self, nombre):
        return nombre in self.funciones

    def agregar_funcion(self, nombre, retorno):
        """
        Registra una funcion nueva con su propia tabla local.

        Returns:
            Funcion o None si el nombre ya existe.
        """
        if nombre in self.funciones:
            return None
        funcion = Funcion(nombre, retorno)
        funcion.variables = TablaVariables(self.memoria, "local")
        self.funciones[nombre] = funcion
        return funcion

    def obtener_funcion(self, nombre):
        return self.funciones.get(nombre)

    def agregar_parametro(self, funcion, nombre, tipo):
        """
        Agrega el parametro a la lista ordenada y a la tabla local.

        Returns:
            bool: False si el nombre esta repetido o coincide con una variable global.
        """
        if not self.agregar_variable(funcion, nombre, tipo):
            return False
        funcion.parametros.append((nombre, tipo))
        return True

    def agregar_variable(self, funcion, nombre, tipo):
        """Agrega una variable, rechazando nombres globales en ambitos locales."""
        if funcion is not self.programa and self.global_.existe(nombre):
            return False
        return funcion.variables.agregar(nombre, tipo)

    def buscar_variable(self, nombre, funcion):
        """
        Busca primero en la tabla de la funcion y luego en la global
        (los nombres locales y globales no pueden coincidir).

        Returns:
            dict {"tipo", "address"} o None si no existe.
        """
        info = funcion.variables.obtener(nombre)
        if info is None:
            info = self.global_.obtener(nombre)
        return info

    def mostrar(self):
        """Texto legible del directorio (para depurar y para la documentacion)."""
        lineas = []
        for f in self.funciones.values():
            if f.nombre == self.nombre_programa:
                etiqueta = "programa"
            else:
                etiqueta = f"funcion -> {f.retorno}"
            params = ", ".join(f"{n}: {t}" for n, t in f.parametros)
            lineas.append(f"{f.nombre} ({etiqueta}) params=[{params}] inicio={f.inicio}")

            if f.retorno_address is not None:
                lineas.append(f"    retorno -> @{f.retorno_address}")
            if f.tamano is not None:
                for segmento, tamanos in f.tamano.items():
                    texto = ", ".join(f"{t}={n}" for t, n in tamanos.items())
                    lineas.append(f"    tamano {segmento}: {texto}")
            for nombre, info in f.variables.variables.items():
                lineas.append(f"    {nombre}: {info['tipo']} @{info['address']}")
        return "\n".join(lineas)
