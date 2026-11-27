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
    """
    Devuelve la fila de cuadruplos como lista de textos, sin los numeros.
    Quita el (GOTO main) inicial y el (END) final, que siempre estan.
    """
    errores, _, fila = analizar_semantica(input_text)
    assert errores == []
    textos = [str(c) for c in fila.cuadruplos]
    assert textos[0].startswith("(GOTO, -, -, ")
    assert textos[-1] == "(END, -, -, -)"
    return textos[1:-1]


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
        "(GOTOF, t2, -, 6)",
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


# ESTATUTOS DE CONTROL Y FUNCIONES
def test_if_else_quadruples():
    resultado = cuadruplos(programa(
        "if (a > 1) { b = 2; } else { b = 3; };"
    ))
    assert resultado == [
        "(>, a, 1, t1)",
        "(GOTOF, t1, -, 6)",
        "(=, 2, -, b)",
        "(GOTO, -, -, 7)",
        "(=, 3, -, b)",
    ]


def test_while_quadruples():
    resultado = cuadruplos(programa(
        "while (a < 10) do { a = a + 1; };"
    ))
    assert resultado == [
        "(<, a, 10, t1)",
        "(GOTOF, t1, -, 7)",
        "(+, a, 1, t2)",
        "(=, t2, -, a)",
        "(GOTO, -, -, 2)",
    ]


def test_function_call_quadruples():
    resultado = cuadruplos("""program demo;
var a : int;
int doble(n : int) [
    var t : int;
    { t = n * 2; return t; }
];
main { a = doble(3) + 1; }
end""")
    assert resultado == [
        "(*, n, 2, t1)",
        "(=, t1, -, t)",
        "(RETURN, t, -, doble)",
        "(ENDFUNC, -, -, -)",
        "(ERA, -, -, doble)",
        "(PARAM, 3, -, n)",
        "(GOSUB, -, -, doble)",
        "(=, doble, -, t2)",
        "(+, t2, 1, t3)",
        "(=, t3, -, a)",
    ]


def test_virtual_addresses_in_quadruples():
    _, _, fila = analizar_semantica(programa("a = 1 + 2;"))
    texto = fila.mostrar_virtual()
    assert "(+, 10000, 10001, 7000)" in texto
    assert "(=, 7000, -, 1000)" in texto


def test_main_inicio_is_first_main_quadruple():
    _, directorio, fila = analizar_semantica(programa(
        "if (a > 1) { b = 2; } else { b = 3; }; "
        "while (a < 10) do { a = a + 1; };"
    ))
    main = directorio.obtener_funcion("demo")
    assert main.inicio == 2
    assert fila.cuadruplos[main.inicio - 1].operador == ">"


def test_function_return_address_is_copied_to_call_temporal():
    _, directorio, fila = analizar_semantica("""program demo;
var a : int;
int doble(n : int) [
    var t : int;
    { t = n * 2; return t; }
];
main { a = doble(3) + 1; }
end""")
    funcion = directorio.obtener_funcion("doble")
    assert funcion.retorno_address == 1001          # global int despues de 'a'
    texto = fila.mostrar_virtual()
    assert "(RETURN, 4001, -, 1001)" in texto
    assert "(=, 1001, -, 7000)" in texto            # main reinicia sus temporales


def test_nested_function_call_uses_separate_return_temporals():
    _, _, fila = analizar_semantica("""program demo;
var a : int;
int suma(n : int, m : int) [
    { return n + m; }
];
int doble(n : int) [
    { return n * 2; }
];
main { a = doble(suma(1, 2)) + 1; }
end""")
    virtual = fila.mostrar_virtual()
    assert "(PARAM, 10001, -, 4000)" in virtual
    assert "(PARAM, 10000, -, 4001)" in virtual
    assert "(GOSUB" in virtual
    # cada funcion tiene su propia global de retorno: suma -> 1001, doble -> 1002
    assert "(=, 1001, -, 7000)" in virtual
    assert "(=, 1002, -, 7001)" in virtual

# DECLARACION E INVOCACION DE FUNCIONES
FUNCIONES = """program demo;
var a : int;
    x : float;
int doble(n : int) [
    var t : int;
    { t = n * 2; return t; }
];
void mostrar(v : float, k : int) [
    { print(v); }
];
main { a = doble(3) + 1; mostrar(2.5, a); }
end"""


def test_goto_main_and_end():
    _, directorio, fila = analizar_semantica(FUNCIONES)
    main = directorio.obtener_funcion("demo")
    primero = fila.cuadruplos[0]
    assert primero.operador == "GOTO"
    assert primero.resultado == main.inicio
    assert fila.cuadruplos[main.inicio - 2].operador == "ENDFUNC"
    assert fila.cuadruplos[-1].operador == "END"


def test_locals_restart_for_each_function():
    """Cada funcion empieza sus locales y temporales en la base del segmento."""
    _, directorio, _ = analizar_semantica(FUNCIONES)
    doble = directorio.obtener_funcion("doble")
    mostrar = directorio.obtener_funcion("mostrar")
    assert doble.variables.obtener("n")["address"] == 4000
    assert doble.variables.obtener("t")["address"] == 4001
    assert mostrar.variables.obtener("v")["address"] == 5000
    assert mostrar.variables.obtener("k")["address"] == 4000


def test_function_sizes_for_era():
    _, directorio, _ = analizar_semantica(FUNCIONES)
    doble = directorio.obtener_funcion("doble")
    assert doble.tamano == {
        "local": {"int": 2, "float": 0, "bool": 0},
        "temporal": {"int": 1, "float": 0, "bool": 0},
    }
    mostrar = directorio.obtener_funcion("mostrar")
    assert mostrar.tamano["local"] == {"int": 1, "float": 1, "bool": 0}
    programa = directorio.obtener_funcion("demo")
    # a, x y la global de retorno de doble
    assert programa.tamano["global"] == {"int": 2, "float": 1, "bool": 0}
    assert programa.tamano["temporal"]["int"] == 2


def test_void_function_has_no_return_global():
    _, directorio, fila = analizar_semantica(FUNCIONES)
    assert directorio.obtener_funcion("mostrar").retorno_address is None
    textos = [str(c) for c in fila.cuadruplos]
    i = textos.index("(ERA, -, -, mostrar)")
    assert textos[i:i + 4] == [
        "(ERA, -, -, mostrar)",
        "(PARAM, 2.5, -, v)",
        "(PARAM, a, -, k)",
        "(GOSUB, -, -, mostrar)",
    ]


def test_error_missing_return():
    r = errores("""program demo;
int f(n : int) [ { print(n); } ];
main { print(f(1)); }
end""")
    assert any("debe regresar un valor" in e for e in r)


# ANIDAMIENTO Y ERRORES EN LLAMADAS
def test_if_inside_while_uses_jump_stack():
    """
    Cada GOTOF se rellena con SU destino aunque las estructuras esten anidadas.
    (Los numeros empiezan en 2 porque el cuadruplo 1 es el GOTO a main.)
    """
    assert cuadruplos(programa(
        "while (a < 3) do { if (a > 0) { b = 1; }; a = a + 1; };"
    )) == [
        "(<, a, 3, t1)",
        "(GOTOF, t1, -, 10)",     # sale del while (10 = END)
        "(>, a, 0, t2)",
        "(GOTOF, t2, -, 7)",      # salta solo el cuerpo del if
        "(=, 1, -, b)",
        "(+, a, 1, t3)",
        "(=, t3, -, a)",
        "(GOTO, -, -, 2)",
    ]


def test_while_inside_if_else():
    assert cuadruplos(programa(
        "if (a > 0) { while (b < 2) do { b = b + 1; }; } else { b = 5; };"
    )) == [
        "(>, a, 0, t1)",
        "(GOTOF, t1, -, 10)",     # al else
        "(<, b, 2, t2)",
        "(GOTOF, t2, -, 9)",      # sale del while
        "(+, b, 1, t3)",
        "(=, t3, -, b)",
        "(GOTO, -, -, 4)",
        "(GOTO, -, -, 11)",       # fin del if (salta el else)
        "(=, 5, -, b)",
    ]


def test_error_wrong_argument_count_inside_expression():
    """Antes tronaba el compilador (pila vacia); ahora es un error semantico."""
    r = errores("""program demo;
var a : int;
int f(n : int) [ { return n; } ];
main { a = f(1, 2) + 1; }
end""")
    assert len(r) == 1 and "espera 1 argumentos y recibió 2" in r[0]


def test_error_void_function_in_expression():
    r = errores("""program demo;
var a : int;
void f() [ { print(1); } ];
main { a = f() + 1; }
end""")
    assert len(r) == 1 and "no regresa valor" in r[0]
