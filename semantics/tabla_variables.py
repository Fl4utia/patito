"""
Tabla de Variables: guarda las variables de UN ambito (el global o el de una funcion).

Estructura:  diccionario  nombre -> {"tipo": ..., "address": ...}

Se eligio un diccionario porque buscar una variable y detectar un nombre
repetido cuesta O(1).
"""


class TablaVariables:
    def __init__(self, memoria=None, ambito="global"):
        """
        Args:
            memoria (MemoriaVirtual): de donde se piden las direcciones.
            ambito (str): "global" (variables del programa) o "local" (de una funcion).
        """
        self.variables = {}
        self.memoria = memoria
        self.ambito = ambito

    def agregar(self, nombre, tipo):
        """
        Agrega una variable y le asigna su direccion virtual.

        Returns:
            bool: False si el nombre ya existe en esta tabla (doble declaracion).
        """
        if nombre in self.variables:
            return False

        direccion = None
        if self.memoria is not None:
            direccion = self.memoria.asignar_variable(self.ambito, tipo)

        self.variables[nombre] = {"tipo": tipo, "address": direccion}
        return True

    def existe(self, nombre):
        return nombre in self.variables

    def obtener(self, nombre):
        """Devuelve {"tipo", "address"} o None si la variable no existe."""
        return self.variables.get(nombre)
