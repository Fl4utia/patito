"""
Pruebas de la parte semantica: cubo, tablas, directorio y validaciones.

No necesitan ANTLR: simulan los eventos que el listener manda al analizador.
    python -m pytest test_semantica.py -v
"""
from semantics.cubo_semantico import CuboSemantico
from semantics.directorio_funciones import DirectorioFunciones
from semantics.analizador import AnalizadorSemantico
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
    a.ambito.tiene_return = True      # simula el 'return' del cuerpo
    a.fin_funcion(5)
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


def test_local_variable_cannot_reuse_global_name():
    a = nuevo_programa()
    a.declarar_variables(["x"], "int", 2)
    a.inicio_funcion("f", "void", 3)
    a.declarar_variables(["x"], "float", 4)

    assert "variable local 'x'" in a.errores[0]
    assert a.ambito.variables.existe("x") is False
    assert a.usar_variable("x", 5) == "int"


def test_parameter_cannot_reuse_global_name():
    a = nuevo_programa()
    a.declarar_variables(["x"], "int", 2)
    a.inicio_funcion("f", "void", 3)
    a.agregar_parametro("x", "float", 4)

    assert "parámetro 'x'" in a.errores[0]
    assert a.ambito.variables.existe("x") is False
    assert a.ambito.parametros == []


def test_local_names_can_repeat_in_different_functions():
    a = nuevo_programa()
    a.inicio_funcion("f", "void", 2)
    a.declarar_variables(["x"], "int", 3)
    a.fin_funcion(4)
    a.inicio_funcion("g", "void", 5)
    a.declarar_variables(["x"], "int", 6)

    assert a.errores == []
    assert a.ambito.variables.existe("x")


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


def test_virtual_memory_restart_and_sizes():
    memoria = MemoriaVirtual()
    memoria.asignar_variable("local", "int")
    memoria.asignar_variable("local", "float")
    memoria.asignar_temporal("bool")
    assert memoria.tamano_funcion() == {
        "local": {"int": 1, "float": 1, "bool": 0},
        "temporal": {"int": 0, "float": 0, "bool": 1},
    }
    memoria.reiniciar_locales()
    assert memoria.asignar_variable("local", "int") == 4000
    assert memoria.asignar_temporal("bool") == 9000


def test_decode_virtual_address():
    assert MemoriaVirtual.decodificar(1000) == ("global", "int", 0)
    assert MemoriaVirtual.decodificar(5002) == ("local", "float", 2)
    assert MemoriaVirtual.decodificar(9001) == ("temporal", "bool", 1)
    assert MemoriaVirtual.decodificar(13004) == ("constante", "string", 4)


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


def ejecutar(fuente, entradas=None):
    from generated.main import analizar_semantica

    errores, directorio, fila = analizar_semantica(fuente)
    assert errores == []
    maquina = MaquinaVirtual(fila, directorio, entradas=entradas)
    maquina.ejecutar()
    return maquina


def test_virtual_machine_int_to_float_assignment():
    """Un int guardado en una variable float se convierte (3 / 2 -> 1.5)."""
    m = ejecutar("program demo; var x:float; main { x=3; print(x/2); } end")
    assert m.salida == [1.5]


def test_virtual_machine_read_and_print():
    m = ejecutar(
        'program demo; var a:int; x:float; main { read(a); read(x); print("suma", a + x); } end',
        entradas=["4", "0.5"],
    )
    assert m.salida == ["suma", 4.5]


def test_virtual_machine_float_parameter_and_locals():
    m = ejecutar(
        "program demo; var r:float; "
        "float prom(a:float, b:float) [ var s:float; { s=a+b; return s/2; } ]; "
        "main { r=prom(3, 4.0); print(r); } end"
    )
    assert m.salida == [3.5]


def test_virtual_machine_recursion_keeps_separate_frames():
    """Cada llamada tiene sus propias locales: fib(10) = 55."""
    m = ejecutar(
        "program demo; "
        "int fib(n:int) [ { if(n<2){return n;} else {return fib(n-1)+fib(n-2);}; } ]; "
        "main { print(fib(10)); } end"
    )
    assert m.salida == [55]


def test_virtual_machine_runtime_missing_return():
    import pytest
    from semantics.maquina_virtual import ErrorEjecucion

    with pytest.raises(ErrorEjecucion, match="sin ejecutar return"):
        ejecutar(
            "program demo; int f(n:int) [ { if(n>0){return n;}; } ]; "
            "main { print(f(0)); } end"
        )


def test_virtual_machine_division_by_zero():
    import pytest
    from semantics.maquina_virtual import ErrorEjecucion

    with pytest.raises(ErrorEjecucion, match="Division entre cero"):
        ejecutar("program demo; var a:int; main { a=0; print(1/a); } end")


def test_virtual_machine_uninitialized_variable():
    import pytest
    from semantics.maquina_virtual import ErrorEjecucion

    with pytest.raises(ErrorEjecucion, match="sin valor asignado"):
        ejecutar("program demo; var a:int; main { print(a); } end")
