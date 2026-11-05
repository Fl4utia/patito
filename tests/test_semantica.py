"""
Pruebas de la parte semantica: cubo, tablas, directorio y validaciones.

No necesitan ANTLR: simulan los eventos que el listener manda al analizador.
    python -m pytest test_semantica.py -v
"""
from semantics.cubo_semantico import CuboSemantico
from semantics.directorio_funciones import DirectorioFunciones
from semantics.listener import AnalizadorSemantico
from semantics.tabla_variables import TablaVariables


def nuevo_programa():
    """Analizador con un programa 'demo' recien iniciado."""
    a = AnalizadorSemantico()
    a.inicio_programa("demo")
    return a


# CUBO SEMANTICO
def test_cube_basic_operations():
    """El cubo reconoce operaciones aritmeticas y rechaza tipos incompatibles."""
    c = CuboSemantico()
    assert c.resultado("int", "int", "+") == "int"
    assert c.resultado("int", "float", ">") == "bool"
    assert c.resultado("int", "float", "=") is None


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


def test_basic_semantic_errors():
    """Detecta una declaracion duplicada y el uso de una variable inexistente."""
    a = nuevo_programa()
    a.declarar_variables(["a"], "int", 2)
    a.declarar_variables(["a"], "float", 3)
    assert "doblemente declarada" in a.errores[0]

    b = nuevo_programa()
    assert b.usar_variable("x", 5) is None
    assert "no declarada" in b.errores[0]
