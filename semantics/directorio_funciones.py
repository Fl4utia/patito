"""
Directorio de Funciones: registro de todas las funciones del programa.

Estructura: diccionario  nombre -> Funcion
Cada Funcion guarda su tipo de retorno, su lista ORDENADA de parametros
(el orden importa para validar las llamadas) y su propia Tabla de Variables.

El programa mismo se registra como una entrada mas: su tabla de variables es
la tabla global.
"""


from .tabla_variables import TablaVariables


class Funcion:
    def __init__(self, nombre, retorno):
        self.nombre = nombre
        self.retorno = retorno # "void", "int", "float" (None para el programa)
        self.parametros = [] # lista ordenada de (nombre, tipo)
        self.variables = TablaVariables()


class DirectorioFunciones:
    def __init__(self, nombre_programa):
        self.nombre_programa = nombre_programa
        self.funciones = {}
        self.funciones[nombre_programa] = Funcion(nombre_programa, None)

    @property
    def global_(self):
        """Tabla de variables globales (la del programa)."""
        return self.funciones[self.nombre_programa].variables

    def existe_funcion(self, nombre):
        return nombre in self.funciones

    def agregar_funcion(self, nombre, retorno):
        """Registra la funcion. Devuelve None si el nombre ya existe."""
        if nombre in self.funciones:
            return None
        self.funciones[nombre] = Funcion(nombre, retorno)
        return self.funciones[nombre]

    def obtener_funcion(self, nombre):
        return self.funciones.get(nombre)

    def agregar_parametro(self, funcion, nombre, tipo):
        """Agrega el parametro a la lista y a la tabla local. False si esta repetido."""
        if not funcion.variables.agregar(nombre, tipo):
            return False
        funcion.parametros.append((nombre, tipo))
        return True

    def buscar_variable(self, nombre, funcion):
        """Busca primero en la tabla de la funcion y luego en la global. None si no existe."""
        info = funcion.variables.obtener(nombre)
        if info is None:
            info = self.global_.obtener(nombre)
        return info

    def mostrar(self):
        """Texto legible del directorio, util para depurar y para la documentacion."""
        lineas = []
        for f in self.funciones.values():
            etiqueta = "programa" if f.nombre == self.nombre_programa else f"funcion -> {f.retorno}"
            params = ", ".join(f"{n}: {t}" for n, t in f.parametros)
            lineas.append(f"{f.nombre} ({etiqueta}) params=[{params}]")
            for nombre, info in f.variables.variables.items():
                lineas.append(f"    {nombre}: {info['tipo']}")
        return "\n".join(lineas)
