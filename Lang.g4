grammar Lang;

// =====================================================================
//  PARSER - Reglas gramaticales (CFG) de BabyDuck
//
//  Convencion: reglas en minuscula = parser, MAYUSCULAS = scanner.
//  "|" con nada despues = epsilon (la regla puede ser vacia).
//  ANTLR4 resuelve solo la recursion izquierda directa (exp, termino) y
//  los prefijos comunes (ids, decls, plist, pargs, alist, expresion) con
//  su lookahead adaptativo ALL(*), por eso se dejan tal cual en la CFG.
// =====================================================================

// ---------------------------------------------------------------------
// ESTRUCTURA DEL PROGRAMA
// ---------------------------------------------------------------------

// Sigue el diagrama <Programa>: program id ; VARS FUNCS main Body end
// Orden fijo: variables globales, luego funciones, luego main.
// EOF obliga a que no haya nada despues de "end" (sin EOF, ANTLR pararia
// de leer en "end" y aceptaria basura al final del archivo).
//   program demo; var a : int; main { a = 1; } end        -> valido
//   program demo; main { } end extra                       -> error (EOF)
//   program demo; main { } var a : int; end                -> error (vars va antes de main)
programa: PROGRAM ID SEMI vars funcs MAIN body END EOF;

// VARS es opcional (diagrama: hay un camino que se salta toda la seccion).
// La alternativa vacia (epsilon) permite programas sin variables.
//   var a : int;      -> con variables
//   (nada)            -> sin variables
vars: VAR decls |;

// Una o mas declaraciones. Es recursion por la derecha: una declaracion,
// o una declaracion seguida de mas.
//   var a : int;
//       x : float;    -> dos declaraciones
decls: decl | decl decls;

// Una declaracion es: lista de ids, dos puntos, tipo y punto y coma.
//   a, b, c : int;
decl: ids COLON tipo SEMI;

// Lista de ids separados por coma (diagrama: lazo con ",").
// Un solo id, o un id, coma y el resto de la lista.
//   a            -> ID
//   a, b, c      -> ID COMMA ids
//   a, : int;    -> error (coma sin id despues)
ids: ID | ID COMMA ids;

// Solo dos tipos de datos (diagrama <TYPE>).
//   string no existe: "var a : string;" es error de sintaxis.
tipo: INT | FLOAT;

// ---------------------------------------------------------------------
// FUNCIONES
// ---------------------------------------------------------------------

// Cero o mas funciones, antes de main.
funcs: func funcs |;

// Diagrama <FUNCS>: (void | TYPE) id ( params ) [ VARS Body ] ;
// - Los corchetes [ ] encierran las variables locales y el cuerpo; las
//   llaves { } son solo del Body. Asi el parser distingue ambos niveles.
// - vars va antes de body: las locales se declaran antes de los estatutos.
// - Termina en ";" como indica el diagrama.
//   void saluda() [ { print("hola"); } ];
//   int doble(n : int) [ var t : int; { t = n * 2; return t; } ];
//   void f() { { } };     -> error (usa llaves en vez de corchetes)
func: rtype ID LPAREN params RPAREN LBRACK vars body RBRACK SEMI;

// Tipo de retorno: void (no devuelve nada) o un tipo (int, float).
rtype: VOID | tipo;

// Parametros opcionales (epsilon = funcion sin parametros).
params: plist |;

// Lista "id : tipo" separados por coma. Cada parametro lleva su tipo.
//   n : int
//   n : int, m : float
//   n : int,         -> error (coma sobrante)
//   n                -> error (falta el tipo)
plist: ID COLON tipo | ID COLON tipo COMMA plist;

// ---------------------------------------------------------------------
// CUERPO Y ESTATUTOS
// ---------------------------------------------------------------------

// Cero o mas estatutos entre llaves (diagrama <Body>).
body: LBRACE stmts RBRACE;
stmts: statement stmts |;

// Un estatuto es cualquiera de estas siete formas (diagrama <STATEMENT>).
// assign y fCall empiezan igual, con un ID. Se distinguen mirando el
// siguiente token: "=" es asignacion, "(" es llamada.
//   a = 5;      -> assign
//   f(5);       -> fCall
statement: assign | condition | cycle | fCall | printStmt | readStmt | returnStmt;

// Asignacion: id = expresion ;
//   a = b + 1;
//   a = ;        -> error (falta la expresion)
//   a = 5        -> error (falta ;)
assign: ID ASSIGN expresion SEMI;

// print acepta una lista de argumentos, y cada uno es una expresion o un
// letrero (string). Los strings SOLO existen aqui: no son una expresion.
//   print("a vale:", a, a * 2);
//   print();         -> error (necesita al menos un argumento)
//   a = "hola";      -> error (un string no es expresion)
printStmt: PRINT LPAREN pargs RPAREN SEMI;
pargs: parg | parg COMMA pargs;
parg: expresion | CTE_STRING;

// read lee a una variable, por eso lleva un ID y no una expresion.
//   read(a);
//   read(3);     -> error
readStmt: READ LPAREN ID RPAREN SEMI;

// return devuelve el valor de una expresion (diagrama <Return>).
// La regla solo revisa la forma; que solo aparezca dentro de funciones y
// con el tipo correcto es tarea de la semantica, no del parser.
//   return n * 2;
//   return;      -> error (falta la expresion)
returnStmt: RETURN expresion SEMI;

// while ( expresion ) do Body ;
// Termina en ";" segun el diagrama <CYCLE>.
//   while (a < 10) do { a = a + 1; };
//   while (a < 10) { ... };   -> error (falta do)
cycle: WHILE LPAREN expresion RPAREN DO body SEMI;

// if ( expresion ) Body [else Body] ;
// elsep es la parte opcional: epsilon cuando no hay else. El ";" va al
// final de todo el if, despues del else si existe.
//   if (a > 1) { a = 0; };
//   if (a > 1) { a = 0; } else { a = 1; };
//   if (a > 1) { a = 0; }     -> error (falta ;)
//   else { ... };             -> error (else sin if)
condition: IF LPAREN expresion RPAREN body elsep SEMI;
elsep: ELSE body |;

// ---------------------------------------------------------------------
// LLAMADAS A FUNCION
// ---------------------------------------------------------------------

// Se separan en dos reglas porque el diagrama <F_Call> termina en ";" pero
// tambien aparece dentro de <FACTOR>, donde no puede llevarlo:
//   call  = id ( args )       -> sin ";", se usa dentro de expresiones
//   fCall = call ;            -> con ";", se usa como estatuto
// Si factor usara fCall (con ;), "a = f(1) + 2;" seria imposible, porque
// la llamada tendria que cerrar con ";" antes del "+".
//   f(1, 2);              -> estatuto (fCall)
//   a = f(1) + 2;         -> call dentro de una expresion
//   f(1)                  -> error como estatuto (falta ;)
fCall: call SEMI;
call: ID LPAREN args RPAREN;

// Argumentos opcionales: f() no lleva ninguno. Si hay, son expresiones
// separadas por coma (no solo ids: f(a + 1, b * 2) es valido).
//   f(1 2);      -> error (falta coma)
args: alist |;
alist: expresion | expresion COMMA alist;

// ---------------------------------------------------------------------
// EXPRESIONES
// La precedencia se logra por niveles: cuanto mas profundo esta un
// operador, mas fuerte liga.
//   expresion (> < !=)  ->  exp (+ -)  ->  termino (* /)  ->  factor
// ---------------------------------------------------------------------

// Una comparacion como maximo (diagrama <EXPRESION>: un solo camino con
// exp rel exp). Por eso "a < b < c" es error de sintaxis.
//   a + 1 > b * 2   -> valido (la aritmetica se resuelve antes de comparar)
//   a < b < c       -> error
expresion: exp | exp rel exp;

// Solo existen >, < y !=. No hay >=, <= ni ==.
//   a >= b  se lee como ">" y luego "=", y falla en el parser.
rel: GT | LT | NEQ;

// Suma y resta. Son recursivas por la IZQUIERDA a proposito: eso hace que
// agrupen de izquierda a derecha, que es lo correcto.
//   10 - 4 - 3   ->  (10 - 4) - 3  =  3     (a la derecha daria 9)
// ANTLR4 acepta recursion izquierda directa y la convierte internamente.
exp: termino | exp PLUS termino | exp MINUS termino;

// Multiplicacion y division, un nivel mas profundo que la suma. Por eso
// ligan mas fuerte: en 2 + 3 * 4 el 3 * 4 se agrupa primero y da 14.
// Tambien recursiva por la izquierda: 100 / 10 / 5 = (100 / 10) / 5 = 2.
termino: factor | termino MULT factor | termino DIV factor;

// Lo mas basico de una expresion:
//   ( expresion )   parentesis, para cambiar la precedencia: (2 + 3) * 4
//   call            llamada a funcion que devuelve valor: f(1) + 2
//   ID              variable
//   cte             constante numerica
//   sign ID / sign cte   con signo unario: -b, +3, a * -2
// Solo se permite UN signo y solo antes de id o constante, tal como el
// diagrama: "--b" es error y "-(a + b)" tambien.
// call va antes que ID aunque no es necesario: ANTLR decide mirando si
// despues del ID viene "(".
factor: LPAREN expresion RPAREN | call | ID | cte | sign ID | sign cte;

// El signo es parte del factor y NO de la constante. Por eso en "a-1" el
// scanner ve ID MINUS CTE_INT (una resta) y no ID seguido de "-1".
sign: PLUS | MINUS;

// Constantes numericas. Los strings no estan aqui: solo van en print.
cte: CTE_INT | CTE_FLOAT;

// =====================================================================
//  SCANNER - Expresiones regulares
//
//  Dos reglas de desempate de ANTLR en el scanner:
//   1) Gana el match mas largo.
//   2) A igual longitud gana la regla que aparece primero.
// =====================================================================

// Palabras reservadas. Van ANTES de ID: "program" cumple la regex de ID
// con la misma longitud, y asi gana la regla de palabra reservada.
// Por la regla 1, un id que solo EMPIEZA con una reservada sigue siendo id:
//   printx, ifa, doo  -> ID (no PRINT + x, IF + a, DO + o)
// read y return aparecen en los diagramas de <STATEMENT>.
PROGRAM: 'program';
MAIN: 'main';
END: 'end';
VAR: 'var';
INT: 'int';
FLOAT: 'float';
VOID: 'void';
PRINT: 'print';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
READ: 'read';
RETURN: 'return';

// Simbolos. NEQ es de dos caracteres ("!="): por la regla del match mas
// largo, "a!=b" da ID NEQ ID. Un "!" solo no pertenece a ningun token y
// el scanner lo reporta como error. No existe ">=" (se lee GT y ASSIGN).
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
GT: '>';
LT: '<';
NEQ: '!=';
SEMI: ';';
COLON: ':';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';

// Constantes e identificadores.
// CTE_FLOAT exige digitos a ambos lados del punto: 3.14 y 0.5 son validos;
// "3." y ".5" no (el "." suelto es un error del scanner). Se lista antes
// que CTE_INT por claridad; "3.14" ya gana por ser el match mas largo.
CTE_FLOAT: [0-9]+ '.' [0-9]+;

// Enteros sin signo; el signo lo maneja el parser (ver regla sign).
CTE_INT: [0-9]+;

// String entre comillas dobles, sin saltos de linea adentro. Todo lo que
// esta dentro (palabras reservadas, simbolos) es parte del string:
//   "if (x) { y = 1; }"  -> UN solo CTE_STRING
// Un string sin cerrar o con salto de linea es error del scanner.
CTE_STRING: '"' ~["\r\n]* '"';

// Id: empieza con letra MINUSCULA y sigue con minusculas, digitos o _.
//   a, abc, x_1_y   -> validos
//   Hola, _x, 1a    -> error del scanner (mayuscula, guion bajo o digito al inicio)
ID: [a-z] [a-z0-9_]*;

// Espacios, tabuladores y saltos de linea: el scanner los descarta y el
// parser nunca los ve, asi "a=b+1;" y "a = b + 1 ;" son equivalentes.
WS: [ \t\r\n]+ -> skip;
