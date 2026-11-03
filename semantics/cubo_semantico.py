"""
Cubo semantico de BabyDuck.

Dice, para un operador y los tipos de sus dos operandos, de que tipo es el
resultado. Si la combinacion no es valida, devuelve None.

Tipos: "int", "float" y "bool". No existen variables bool: bool solo es el
resultado de una comparacion (sirve para las condiciones de if y while).
"""


ERROR = None

# Operadores aritmeticos: si algun operando es float, el resultado es float.
_ARITMETICA = {
    ("int", "int"): "int",
    ("int", "float"): "float",
    ("float", "int"): "float",
    ("float", "float"): "float",
}

# Comparaciones: cualquier mezcla de int y float da bool.
_COMPARACION = {par: "bool" for par in _ARITMETICA}

# Asignacion (variable izquierda = expresion derecha):
# un int no puede recibir un float porque se perderia la parte decimal.
_ASIGNACION = {
    ("int", "int"): "int",
    ("int", "float"): ERROR,
    ("float", "int"): "float",
    ("float", "float"): "float",
}

_TABLAS = {
    "+": _ARITMETICA, "-": _ARITMETICA, "*": _ARITMETICA, "/": _ARITMETICA,
    ">": _COMPARACION, "<": _COMPARACION, "!=": _COMPARACION,
    "=": _ASIGNACION,
}


class CuboSemantico:
    """Consulta el cubo: resultado(izq, der, operador) -> tipo o None."""

    def resultado(self, izq, der, operador):
        tabla = _TABLAS.get(operador)
        if tabla is None:
            return ERROR
        return tabla.get((izq, der), ERROR)