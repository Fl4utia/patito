"""
Test-Plan 

Como correrlo (despues de generar el codigo con ANTLR):
    pip install pytest
    python -m pytest test_babyduck.py -v
"""
from generated.main import analizar_texto


# Funciones de apoyo
def tipos(input_text):
    """Devuelve los tipos de token que reconoce el scanner."""
    return [tipo for tipo, _ in analizar_texto(input_text)["tokens"]]


def es_valido(input_text):
    """True si el scanner y el parser no reportan ningun error."""
    r = analizar_texto(input_text)
    return not r["lex_errors"] and not r["syn_errors"]


def hay_error_lexico(input_text):
    """True si el scanner reporta al menos un error."""
    return bool(analizar_texto(input_text)["lex_errors"])


def hay_error_sintaxis(input_text):
    """True si el scanner no reporta nada pero el parser si."""
    r = analizar_texto(input_text)
    return not r["lex_errors"] and bool(r["syn_errors"])


# SCANNER 
def test_scanner_reserved_words():
    """Cada palabra reservada se reconoce con su propio token."""
    input_text = "program main end var int float void print if else while do read return"
    assert tipos(input_text) == [
        "PROGRAM", "MAIN", "END", "VAR", "INT", "FLOAT", "VOID", "PRINT",
        "IF", "ELSE", "WHILE", "DO", "READ", "RETURN",
    ]


def test_scanner_identifiers_and_numbers():
    """Ids, enteros y flotantes. 'printx' es un id, no PRINT seguido de x."""
    input_text = "abc x_1 printx 7 3.14"
    assert tipos(input_text) == ["ID", "ID", "ID", "CTE_INT", "CTE_FLOAT"]


def test_scanner_illegal_characters():
    """Un caracter que no pertenece a ningun token ('$') es error lexico."""
    input_text = """
    program demo;
    var total : int;
    main {
        total = 4 $ 2;
    }
    end
    """
    assert hay_error_lexico(input_text), "El scanner debio rechazar el '$'."


#Caso porpoio de mi lengauje (Defini que las variables deben comenzar con minuscula y no pueden contener mayusculas)
def test_scanner_rejects_uppercase_variable_names():
    """Los nombres de variables deben comenzar con una letra minuscula y no pueden contener mayusculas."""
    input_text = """
    program demo;
    var Total : int;
    main { }
    end
    """
    assert hay_error_lexico(input_text), "El scanner debio rechazar 'Total'."


# PARSER 
#   Programas validos: variables, expresiones, condicionales y ciclos,
#   print/read y funciones.  Programas con error: nombres test_error_*
def test_variable_declarations():
    """Programa con variables y asignaciones se acepta."""
    input_text = """
    program demo;
    var a, b : int;
        x : float;
    main {
        a = 5;
        b = a + 3;
        x = 3.14;
    }
    end
    """
    assert es_valido(input_text)


def test_arithmetic_expressions():
    """Operadores, parentesis y signos unarios en una expresion."""
    input_text = """
    program demo;
    var a, b, c : int;
    main {
        c = a + b * 4 - (a - b) / 2;
        a = -b;
    }
    end
    """
    assert es_valido(input_text)


def test_conditional_and_loop_statements():
    """Condicion con else y un ciclo while se aceptan."""
    input_text = """
    program demo;
    var a, b : int;
    main {
        if (a > b) { a = 0; } else { a = 1; };
        while (a < 10) do { a = a + 1; };
    }
    end
    """
    assert es_valido(input_text)


def test_print_and_read_statements():
    """print con strings y expresiones, y read con un id."""
    input_text = """
    program demo;
    var a : int;
    main {
        read(a);
        print("a vale:", a, a * 2);
    }
    end
    """
    assert es_valido(input_text)


def test_function_with_return():
    """Funcion con parametros y return; se llama dentro de una expresion."""
    input_text = """
    program demo;
    var a : int;
    int doble(n : int) [
        { return n * 2; }
    ];
    main {
        a = doble(3) + 1;
    }
    end
    """
    assert es_valido(input_text)


def test_void_function_with_locals():
    """Funcion void con parametros y variables locales, llamada como estatuto."""
    input_text = """
    program demo;
    void muestra(n : int, m : float) [
        var temp : int;
        {
            temp = n + 1;
            print("valores:", temp, m);
        }
    ];
    main {
        muestra(2, 1.5);
    }
    end
    """
    assert es_valido(input_text)


def test_error_missing_semicolon():
    """Una asignacion sin ';' es error de sintaxis."""
    input_text = """
    program demo;
    var a : int;
    main {
        a = 5
    }
    end
    """
    assert hay_error_sintaxis(input_text), "Debio fallar por el ';' faltante."


def test_error_missing_end():
    """Un programa sin 'end' al final es error de sintaxis."""
    input_text = """
    program demo;
    main {
    }
    """
    assert hay_error_sintaxis(input_text), "Debio fallar porque falta 'end'."


def test_error_variables_after_main():
    """Las variables deben declararse antes de main, no despues."""
    input_text = """
    program demo;
    main {
    }
    var a : int;
    end
    """
    assert hay_error_sintaxis(input_text), "Debio fallar: 'var' va antes de 'main'."


def test_error_incomplete_expression():
    """Una asignacion sin expresion ('a = ;') es error de sintaxis."""
    input_text = """
    program demo;
    var a : int;
    main {
        a = ;
    }
    end
    """
    assert hay_error_sintaxis(input_text), "Debio fallar por la expresion vacia."


def test_error_loop_without_do():
    """Un while sin la palabra 'do' es error de sintaxis."""
    input_text = """
    program demo;
    var a : int;
    main {
        while (a < 10) { a = a + 1; };
    }
    end
    """
    assert hay_error_sintaxis(input_text), "Debio fallar porque falta 'do'."