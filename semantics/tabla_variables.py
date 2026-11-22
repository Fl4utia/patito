"""
Tabla de Variables: guarda las variables de UN ambito (el global o el de una funcion).

Estructura: diccionario  nombre -> {"tipo": ..., "address": ...}
Se eligio un diccionario porque buscar y detectar un nombre repetido cuesta O(1).
"address" queda en None hasta que se implemente la memoria virtual.
"""


class TablaVariables:
    def __init__(self, memoria=None, ambito="global"):
        self.variables = {}
        self.memoria = memoria
        self.ambito = ambito

    def agregar(self, nombre, tipo):
        """Agrega la variable. Devuelve False si el nombre ya existe en esta tabla."""
        if nombre in self.variables:
            return False
        address = None
        if self.memoria is not None:
            address = self.memoria.asignar_variable(self.ambito, tipo)
        self.variables[nombre] = {"tipo": tipo, "address": address}
        return True

    def existe(self, nombre):
        return nombre in self.variables

    def obtener(self, nombre):
        """Devuelve {"tipo", "address"} o None si no existe."""
        return self.variables.get(nombre)
