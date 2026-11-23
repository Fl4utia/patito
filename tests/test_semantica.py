"""
Pruebas de la parte semantica: cubo, tablas, directorio y validaciones.

No necesitan ANTLR: simulan los eventos que el listener manda al analizador.
    python -m pytest test_semantica.py -v
"""
from semantics.cubo_semantico import CuboSemantico
from semantics.directorio_funciones import DirectorioFunciones
from semantics.listener import AnalizadorSemantico
from semantics.tabla_variables import TablaVariables
from semantics.memoria_virtual import MemoriaVirtual
from semantics.maquina_virtual import MaquinaVirtual


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


# DIRECCIONES VIRTUALES
def test_virtual_address_segments():
    memoria = MemoriaVirtual()
    assert memoria.asignar_variable("global", "int") == 1000
    assert memoria.asignar_variable("global", "float") == 2000
    assert memoria.asignar_variable("local", "int") == 4000
    assert memoria.asignar_temporal("int") == 7000
    assert memoria.asignar_temporal("float") == 8000
    assert memoria.asignar_constante("3", "int") == 10000
    assert memoria.asignar_constante("3.14", "float") == 11000
    assert memoria.asignar_constante("hola", "string") == 13000


def test_virtual_machine_arithmetic_and_assignment():
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(
        "program demo; var a:int; main { a=2*3+1; } end"
    )
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio)
    maquina.ejecutar()
    assert maquina.globales[1000] == 7


def test_virtual_machine_if_and_while():
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(
        "program demo; var a,b:int; main { "
        "a=0; while(a<3) do {a=a+1;}; "
        "if(a>2){b=10;}else{b=20;}; "
        "} end"
    )
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio)
    maquina.ejecutar()
    assert maquina.globales[1000] == 3
    assert maquina.globales[1001] == 10


def test_virtual_machine_function_return():
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(
        "program demo; var a:int; "
        "int doble(n:int) [ var t:int; { t=n*2; return t; } ]; "
        "main { a=doble(3)+1; } end"
    )
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio)
    maquina.ejecutar()
    assert maquina.globales[1000] == 7


def test_virtual_machine_nested_function_calls():
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(
        "program demo; var a:int; "
        "int suma(n:int,m:int) [ { return n+m; } ]; "
        "int doble(n:int) [ { return n*2; } ]; "
        "main { a=doble(suma(1,2))+1; } end"
    )
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio)
    maquina.ejecutar()
    assert maquina.globales[1000] == 7


def test_virtual_machine_void_function():
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(
        "program demo; var a:int; "
        "void poner() [ { a=9; } ]; "
        "main { poner(); } end"
    )
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio)
    maquina.ejecutar()
    assert maquina.globales[1000] == 9


def test_virtual_machine_recursive_function():
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(
        "program demo; var a:int; "
        "int fact(n:int) [ "
        "{ if(n<2){return 1;} else {return n*fact(n-1);}; } ]; "
        "main { a=fact(3); } end"
    )
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio)
    maquina.ejecutar()
    assert maquina.globales[1000] == 6
