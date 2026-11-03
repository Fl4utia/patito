"""
Pruebas de la parte semantica: cubo, tablas, directorio y validaciones.

No necesitan ANTLR: simulan los eventos que el listener manda al analizador.
    python -m pytest test_semantica.py -v
"""
from cubo_semantico import CuboSemantico
from directorio_funciones import DirectorioFunciones
from listener import AnalizadorSemantico
from tabla_variables import TablaVariables


def nuevo_programa():
    """Analizador con un programa 'demo' recien iniciado."""
    a = AnalizadorSemantico()
    a.inicio_programa("demo")
    return a


# CUBO SEMANTICO
def test_cube_arithmetic_operations():
    """Aritmetica: int con int da int; si hay un float, el resultado es float."""
    c = CuboSemantico()
    assert c.resultado("int", "int", "+") == "int"
    assert c.resultado("int", "float", "-") == "float"
    assert c.resultado("float", "int", "*") == "float"
    assert c.resultado("int", "int", "/") == "int"


def test_cube_comparison_and_assignment():
    """Comparaciones dan bool; asignar un float a un int es error."""
    c = CuboSemantico()
    assert c.resultado("int", "float", ">") == "bool"
    assert c.resultado("float", "float", "!=") == "bool"
    assert c.resultado("float", "int", "=") == "float"
    assert c.resultado("int", "float", "=") is None
    assert c.resultado("bool", "int", "+") is None      # bool no se puede operar


# ESTRUCTURAS DE DATOS
def test_variable_table_add_and_lookup():
    """La tabla guarda tipo por nombre y rechaza un nombre repetido."""
    t = TablaVariables()
    assert t.agregar("a", "int") is True
    assert t.agregar("a", "float") is False
    assert t.obtener("a")["tipo"] == "int"
    assert t.obtener("z") is None


def test_function_directory_add_and_lookup():
    """El directorio guarda funciones con parametros en orden y rechaza duplicadas."""
    d = DirectorioFunciones("demo")
    f = d.agregar_funcion("suma", "int")
    assert d.agregar_funcion("suma", "void") is None
    d.agregar_parametro(f, "x", "int")
    d.agregar_parametro(f, "y", "float")
    assert d.obtener_funcion("suma").parametros == [("x", "int"), ("y", "float")]


# VALIDACIONES (puntos neuralgicos)
def test_valid_program_has_no_semantic_errors():
    """Un programa bien formado llena el directorio y no reporta errores."""
    a = nuevo_programa()
    a.declarar_variables(["a", "b"], "int", 2)
    a.inicio_funcion("doble", "int", 3)
    a.agregar_parametro("n", "int", 3)
    assert a.usar_variable("n", 4) == "int"
    a.fin_funcion()
    assert a.llamar_funcion("doble", 8) is not None
    assert a.errores == []
    assert set(a.directorio.funciones) == {"demo", "doble"}


def test_error_variable_declared_twice():
    """Declarar dos veces el mismo nombre en el mismo ambito es error."""
    a = nuevo_programa()
    a.declarar_variables(["a"], "int", 2)
    a.declarar_variables(["a"], "float", 3)
    assert len(a.errores) == 1 and "doblemente declarada" in a.errores[0]


def test_error_function_declared_twice():
    """Declarar dos funciones con el mismo nombre es error."""
    a = nuevo_programa()
    a.inicio_funcion("f", "void", 2)
    a.fin_funcion()
    a.inicio_funcion("f", "int", 5)
    a.fin_funcion()
    assert len(a.errores) == 1 and "función 'f' doblemente declarada" in a.errores[0]


def test_error_repeated_parameter():
    """Dos parametros con el mismo nombre en una funcion es error."""
    a = nuevo_programa()
    a.inicio_funcion("f", "void", 2)
    a.agregar_parametro("n", "int", 2)
    a.agregar_parametro("n", "float", 2)
    assert len(a.errores) == 1 and "repetido" in a.errores[0]


def test_error_undeclared_variable():
    """Usar una variable que no se declaro es error."""
    a = nuevo_programa()
    assert a.usar_variable("x", 5) is None
    assert len(a.errores) == 1 and "no declarada" in a.errores[0]


def test_error_undeclared_function():
    """Llamar a una funcion que no existe es error."""
    a = nuevo_programa()
    assert a.llamar_funcion("fantasma", 6) is None
    assert len(a.errores) == 1 and "función 'fantasma' no declarada" in a.errores[0]


def test_local_variable_shadows_global():
    """Una variable local puede llamarse igual que una global y tiene prioridad."""
    a = nuevo_programa()
    a.declarar_variables(["x"], "int", 2)
    a.inicio_funcion("f", "void", 3)
    a.declarar_variables(["x"], "float", 4)
    assert a.usar_variable("x", 5) == "float"      # dentro de f gana la local
    a.fin_funcion()
    assert a.usar_variable("x", 9) == "int"        # fuera de f vuelve la global
    assert a.errores == []


def test_local_variable_not_visible_outside_function():
    """Al salir de una funcion, sus variables locales ya no se ven."""
    a = nuevo_programa()
    a.inicio_funcion("f", "void", 2)
    a.declarar_variables(["temp"], "int", 3)
    a.fin_funcion()
    assert a.usar_variable("temp", 8) is None
    assert len(a.errores) == 1
