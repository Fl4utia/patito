"""
Pruebas de la generacion de cuadruplos (expresiones y estatutos lineales).

Como correrlo (despues de generar el codigo con ANTLR):
    python -m pytest tests/test_cuadruplos.py -v
"""
from generated.main import analizar_semantica


# Funciones de apoyo
def programa(cuerpo):
    """Arma un programa completo con a, b: int y x: float, y 'cuerpo' dentro de main."""
    return f"""program demo;
var a, b : int;
    x : float;
main {{
    {cuerpo}
}}
end"""


def cuadruplos(input_text):
    """Devuelve la fila de cuadruplos como lista de textos, sin los numeros."""
    errores, _, fila = analizar_semantica(input_text)
    assert errores == []
    return [str(c) for c in fila.cuadruplos]


def errores(input_text):
    """Devuelve los errores semanticos que se reportaron."""
    return analizar_semantica(input_text)[0]


# EXPRESIONES ARITMETICAS
def test_arithmetic_precedence():
    """La multiplicacion se resuelve antes que la suma."""
    assert cuadruplos(programa("a = 1 + 2 * 3;")) == [
        "(*, 2, 3, t1)",
        "(+, 1, t1, t2)",
        "(=, t2, -, a)",
    ]


def test_arithmetic_parentheses():
    """Los parentesis cambian el orden: primero la suma."""
    assert cuadruplos(programa("a = (1 + 2) * 3;")) == [
        "(+, 1, 2, t1)",
        "(*, t1, 3, t2)",
        "(=, t2, -, a)",
    ]


def test_arithmetic_left_to_right():
    """Con la misma precedencia se resuelve de izquierda a derecha: (a - 2) - 1."""
    assert cuadruplos(programa("b = a - 2 - 1;")) == [
        "(-, a, 2, t1)",
        "(-, t1, 1, t2)",
        "(=, t2, -, b)",
    ]


def test_arithmetic_unary_minus():
    """El menos unario se traduce como 0 - valor."""
    assert cuadruplos(programa("x = -a + 2.5;")) == [
        "(-, 0, a, t1)",
        "(+, t1, 2.5, t2)",
        "(=, t2, -, x)",
    ]


# EXPRESIONES RELACIONALES
def test_relational_expression():
    """La comparacion se hace despues de resolver la aritmetica de ambos lados."""
    assert cuadruplos(programa("if (a + 1 > b) { a = 1; };")) == [
        "(+, a, 1, t1)",
        "(>, t1, b, t2)",
        "(=, 1, -, a)",
    ]


# ESTATUTOS LINEALES
def test_linear_statements():
    """print, read y asignacion generan sus cuadruplos en el orden del programa."""
    assert cuadruplos(programa('read(a); print("a vale", a * 2);')) == [
        "(READ, -, -, a)",
        '(PRINT, -, -, "a vale")',
        "(*, a, 2, t1)",
        "(PRINT, -, -, t1)",
    ]


# ERRORES DE TIPOS
def test_error_incompatible_assignment():
    """Asignar un float a una variable int es error (segun el cubo)."""
    r = errores(programa("a = 2.5;"))
    assert len(r) == 1 and "no se puede asignar float a 'a' (int)" in r[0]


def test_error_no_cascade_for_undeclared_variable():
    """Una variable no declarada da un solo error, sin errores en cadena ni cuadruplos."""
    r = errores(programa("a = z + 1;"))
    assert len(r) == 1 and "variable 'z' no declarada" in r[0]