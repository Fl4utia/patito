# BabyDuck / Patito

Compilador en construcción para el lenguaje BabyDuck. El proyecto implementa
el scanner, el parser, el análisis semántico y una primera generación de
cuádruplos usando [ANTLR4](https://www.antlr.org/) y Python.

## Requisitos

- Python 3.10 o posterior.
- Java, necesario para ejecutar la herramienta de ANTLR y regenerar el código.
- `pip`.

El repositorio ya contiene un entorno virtual local (`.venv`) y el código
generado en `generated/`. Si se usa otro entorno, instala las dependencias:

```bash
python -m venv .venv
source .venv/bin/activate  

python -m pip install antlr4-python3-runtime antlr4-tools pytest
```

## Regenerar lexer y parser

La gramática fuente está en [`Lang.g4`](./Lang.g4). Cada vez que se cambien
sus reglas, desde la raíz del repositorio ejecuta:

```bash
antlr4 -Dlanguage=Python3 -o generated Lang.g4
```

Esto actualiza `LangLexer.py`, `LangParser.py`, `LangListener.py` y los
archivos auxiliares dentro de `generated/`. La generación requiere Java.

## Cómo ejecutar un programa

Los programas se guardan en archivos de texto. Por ejemplo,
[`tests/prueba.txt`](./tests/prueba.txt) contiene un programa válido:

```bash
python -m generated.main tests/prueba.txt
```

Si todo está correcto, se muestra:

```text
[OK] tests/prueba.txt: programa válido
```

El módulo debe ejecutarse con `-m` desde la raíz para que funcionen los
paquetes `generated` y `semantics`.

### Opciones de salida

Las opciones pueden combinarse:

```bash
# Lista los tokens reconocidos por el scanner
python -m generated.main tests/prueba.txt --tokens

# Imprime el árbol de derivación
python -m generated.main tests/prueba.txt --tree

# Imprime el directorio de funciones y sus tablas de variables
python -m generated.main tests/prueba.txt --tables

# Imprime la fila de cuádruplos generada
python -m generated.main tests/prueba.txt --cuadruplos

# Ejemplo completo
python -m generated.main tests/prueba.txt --tokens --tree --tables --cuadruplos
```

El programa se detiene antes del análisis semántico si encuentra errores
léxicos o de sintaxis. Si encuentra errores semánticos, los reporta y tampoco
imprime tablas ni cuádruplos.

## Flujo del compilador

### 1. Scanner (lexer)

El lexer lee el texto carácter por carácter y lo transforma en tokens:
`program`, `a`, `=`, `5`, `;`, etc. Las reglas en MAYÚSCULAS de
[`Lang.g4`](./Lang.g4) definen las palabras reservadas, símbolos, constantes e
identificadores. ANTLR genera el scanner en `generated/LangLexer.py`.

Si aparece un carácter que no pertenece al lenguaje, por ejemplo `$`, se
reporta un error léxico.

Los identificadores deben comenzar con una letra minúscula y pueden continuar
con letras minúsculas, dígitos o `_`. Los tipos disponibles son `int` y
`float`; los strings solo se aceptan como argumentos de `print`.

### 2. Parser

El parser recibe los tokens y comprueba su orden según las reglas en
minúsculas de [`Lang.g4`](./Lang.g4). Un `;` faltante, un `end` adicional o una
sección fuera de orden producen un error de sintaxis.

El parser construye un árbol de derivación. La estructura de la gramática
resuelve la precedencia y asociatividad:

1. Paréntesis.
2. Multiplicación y división.
3. Suma y resta.
4. Comparaciones (`>`, `<`, `!=`).

### 3. Listener y análisis semántico

`ParseTreeWalker` recorre el árbol. Al entrar y salir de cada regla de ANTLR
invoca métodos `enterX` y `exitX` de `ListenerSemantico`, implementado en
[`semantics/listener.py`](./semantics/listener.py).

El listener conecta cada nodo con el analizador semántico y con el generador de
cuádruplos. El punto de entrada de la ejecución está en
[`generated/main.py`](./generated/main.py).

### 4. Estructuras semánticas

- **Directorio de funciones:** registra cada función, su tipo de retorno, sus
  parámetros en orden y su tabla de variables. El programa también se registra
  como una entrada; su tabla representa el ámbito global.
- **Tabla de variables:** guarda el tipo de cada variable dentro de un ámbito.
  Una variable local o un parámetro puede ocultar una variable global con el
  mismo nombre.
- **Cubo semántico:** recibe los tipos de dos operandos y un operador. Devuelve
  el tipo resultante o `None` si la operación no es válida.
- **Pilas:** se mantienen pilas paralelas de operandos y tipos, además de una
  pila de operadores.
- **Fila de cuádruplos:** conserva las instrucciones en el orden en que se
  generan.

### 5. Validaciones semánticas actuales

El analizador reporta:

1. Variables doblemente declaradas en el mismo ámbito.
2. Funciones doblemente declaradas.
3. Parámetros repetidos.
4. Variables no declaradas.
5. Funciones no declaradas.
6. Uso de una variable local antes que una global con el mismo nombre.
7. Asignaciones, operaciones, condiciones y retornos incompatibles según el
   cubo semántico.

Los errores de una variable no declarada se propagan como un tipo interno
`error` para evitar una cascada de errores y no generar cuádruplos inválidos.

### 6. Generación de cuádruplos

Para una expresión:

1. Cada constante o variable se apila junto con su tipo.
2. Cada operador se apila al entrar al nodo correspondiente del árbol.
3. Al salir del nodo, se sacan dos operandos y el operador.
4. Se consulta el cubo semántico.
5. Si la operación es válida, se crea un temporal (`t1`, `t2`, ...) y se agrega
   el cuádruplo a la fila.

Los paréntesis usan `(` como fondo falso de la pila de operadores. También se
generan cuádruplos para:

- Asignación: `(=, valor, -, variable)`.
- `print`: `(PRINT, -, -, valor)`.
- `read`: `(READ, -, -, variable)`.
- `return`: `(RETURN, -, -, valor)`.
- Operaciones aritméticas y comparaciones.

Ejemplo:

```text
a = 1 + 2 * 3;
```

se convierte en:

```text
  1  (*, 2, 3, t1)
  2  (+, 1, t1, t2)
  3  (=, t2, -, a)
```

### 7. Salida de `main.py`

[`generated/main.py`](./generated/main.py) ejecuta las etapas en este orden:

1. Lee el archivo fuente.
2. Ejecuta scanner y parser.
3. Reporta errores léxicos o sintácticos y se detiene si existen.
4. Ejecuta el listener y el análisis semántico.
5. Reporta errores semánticos y se detiene si existen.
6. Imprime tablas o cuádruplos si se solicitaron.
7. Muestra `[OK]` si el programa es válido.

## Sintaxis básica

```text
program demo;
var a, b : int;
    x : float;

int doble(n : int) [
    var t : int;
    {
        t = n * 2;
        return t;
    }
];

main {
    a = doble(3) + 1;
    x = 2.5;
    print("resultado:", a, x);
    read(a);
}
end
```

Se soportan declaraciones globales y locales, funciones `void`, funciones con
retorno `int` o `float`, parámetros, asignaciones, llamadas, `print`, `read`,
`return`, `if/else` y `while ... do`.

## Pruebas

Ejecuta toda la suite desde la raíz:

```bash
python -m pytest -q
```

También se pueden ejecutar por área:

```bash
python -m pytest tests/test_scanner.py -v
python -m pytest tests/test_semantica.py -v
python -m pytest tests/test_cuadruplos.py -v
```

Las pruebas cubren el scanner, el parser, las tablas semánticas, el cubo, las
validaciones y la generación de cuádruplos para expresiones y estatutos
lineales.

## Direcciones virtuales

Cada variable, constante y temporal recibe una dirección fija dentro de un
segmento. Las direcciones permiten que los cuádruplos se ejecuten sin depender
del nombre original de los identificadores.

| Segmento | `int` | `float` | `bool` | `string` |
|---|---:|---:|---:|---:|
| Global | 1000-1999 | 2000-2999 | 3000-3999 | 13000-13999 |
| Local | 4000-4999 | 5000-5999 | 6000-6999 | 13000-13999 |
| Temporal | 7000-7999 | 8000-8999 | 9000-9999 | No aplica |
| Constante | 10000-10999 | 11000-11999 | 12000-12999 | 13000-13999 |

Cada segmento mantiene un contador independiente. `TablaVariables` guarda
`{"tipo": ..., "address": ...}`, las constantes iguales reutilizan dirección y
los temporales reciben una dirección al crearse. La fila también conserva
`mostrar_virtual()` para inspeccionar los operandos ya traducidos.

```text
a = 1 + 2;

(+, 10000, 10001, 7000)
(=, 7000, -, 1000)
```

## Puntos neurálgicos y flujo general

```text
┌────────────┐  caracteres  ┌───────┐  tokens  ┌────────┐
│ Código     │ ───────────> │ Lexer │ ───────> │ Parser │
└────────────┘              └───────┘          └────┬───┘
                                                   │ árbol
                                                   v
                                         ┌─────────────────┐
                                         │ Listener       │
                                         └───┬─────────┬───┘
                                             │         │
                                      tablas/types   pilas
                                             │         │
                                             v         v
                                      ┌─────────┐  ┌─────────┐
                                      │ Directorio│  │Cubo     │
                                      └────┬────┘  └────┬────┘
                                           │              │
                                           v              v
                                         ┌────────────────┐
                                         │ FilaCuadruplos │
                                         └────────────────┘
```

### Expresiones

```text
enterFactor / exitFactor
        │
        │ variable o constante
        v
[operandos] [tipos] [direcciones]
        │
        v
enterTermino / enterExp / enterExpresion
        │
        │ apila operador
        v
exitTermino / exitExp / exitExpresion
        │
        │ saca operandos y operador
        v
consulta CuboSemantico
        │
        ├─ tipo válido -> crea temporal y agrega cuadruplo
        └─ tipo inválido -> reporta error y propaga "error"
```

### `if / else`

```text
enterCondition
    -> crea marco en pila de condiciones

exitExpresion
    -> reduce la condición
    -> agrega GOTOF(condición, -, salto pendiente)

enterElsep
    -> rellena GOTOF con el inicio del else
    -> agrega GOTO pendiente

exitCondition
    -> rellena GOTO con la siguiente instrucción
```

Sin `else`, `GOTOF` se rellena al terminar el cuerpo. Los números del salto
son índices de instrucciones de la fila, no direcciones virtuales.

### `while ... do`

```text
enterCycle
    -> guarda la siguiente instrucción como inicio del ciclo

exitExpresion
    -> agrega GOTOF(condición, -, salida pendiente)

exitCycle
    -> agrega GOTO hacia el inicio
    -> rellena GOTOF con la siguiente instrucción
```

### Declaración de función

```text
enterFunc
    -> registra nombre y tipo de retorno
    -> activa el ámbito local
    -> agrega parámetros con direcciones locales
    -> guarda el inicio de la función

exitDecl
    -> asigna direcciones a las variables locales

exitReturnStmt
    -> valida el tipo contra el retorno de la función
    -> agrega RETURN

exitFunc
    -> agrega ENDFUNC
    -> restaura el ámbito global
```

### Invocación de función

```text
enterCall
    -> valida que la función exista
    -> agrega ERA
    -> guarda el tamaño de las pilas

exitExpresion (argumentos)
    -> deja una dirección por cada argumento

exitCall
    -> valida número y tipos
    -> agrega PARAM por argumento
    -> agrega GOSUB
    -> crea temporal si la función tiene retorno
```

Los cuádruplos especiales principales son:

| Operador | Significado |
|---|---|
| `GOTOF` | Si la condición es falsa, salta a la instrucción indicada. |
| `GOTO` | Salta incondicionalmente. |
| `ERA` | Reserva el registro de activación de la función llamada. |
| `PARAM` | Entrega un argumento a un parámetro. |
| `GOSUB` | Transfiere control a la función. |
| `RETURN` | Regresa el resultado de una función. |
| `ENDFUNC` | Marca el final de la función. |

## Máquina Virtual

La Máquina Virtual interpreta la fila de cuádruplos. El contador de programa
`ip` indica el cuádruplo actual y avanza o cambia por `GOTO`, `GOTOF`,
`GOSUB`, `RETURN` y `ENDFUNC`.

```text
┌──────────────────────────────────────────────────────────────┐
│                         CUÁDRUPLOS                            │
└──────────────────────────────┬───────────────────────────────┘
                               │ ip
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                     MaquinaVirtual                           │
├──────────────┬──────────────┬──────────────┬────────────────┤
│ Memoria      │ Memoria      │ Pila de      │ Pila de        │
│ global       │ constante    │ frames       │ retornos       │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

### Memoria de ejecución

```text
Direcciones globales        Direcciones locales/temporales
┌────────────────────┐      ┌────────────────────────────────┐
│ 1000-3999 global   │      │ frame activo                   │
│ 1000 int           │      │ 4000-4999  int local           │
│ 2000 float         │      │ 5000-5999  float local         │
│ 3000 bool          │      │ 6000-6999  bool local          │
└────────────────────┘      │ 7000-7999  temporal int        │
                            │ 8000-8999  temporal float      │
                            │ 9000-9999  temporal bool       │
                            └────────────────────────────────┘

Direcciones constantes
┌────────────────────────────────┐
│ 10000-10999  constantes int    │
│ 11000-11999  constantes float  │
│ 12000-12999  constantes bool   │
│ 13000-13999  strings           │
└────────────────────────────────┘
```

### Registro de Activación

Cada `ERA` crea un registro pendiente y cada `GOSUB` activa el último registro:

```text
┌─────────────────────────────────┐
│ Registro de Activación          │
├─────────────────────────────────┤
│ nombre de función               │
│ dirección de inicio             │
│ dirección de retorno            │
│ parámetros locales              │
│ variables locales               │
│ temporales locales              │
│ siguiente instrucción llamador  │
└─────────────────────────────────┘
```

Las llamadas recursivas crean un nuevo frame y conservan las direcciones
locales de cada activación por separado.

### Flujo de una función

```text
ERA ──> crear frame pendiente
PARAM ──> copiar argumento a parámetro
GOSUB ──> guardar retorno y activar frame
RETURN ──> guardar valor y regresar al llamador
ENDFUNC ──> retirar frame
```
