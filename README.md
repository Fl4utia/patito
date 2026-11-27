# BabyDuck / Patito

Compilador en construcción para el lenguaje BabyDuck. El proyecto implementa
el scanner, el parser, el análisis semántico, la generación de cuádruplos con
direcciones virtuales (incluyendo funciones) y una máquina virtual que los
ejecuta, usando [ANTLR4](https://www.antlr.org/) y Python.

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

# Imprime los cuádruplos con direcciones virtuales
python -m generated.main tests/prueba.txt --virtual

# Ejecuta el programa en la máquina virtual
python -m generated.main tests/prueba.txt --run

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

El listener no tiene lógica propia: solo decide en qué momento llamar a las
otras clases. El punto de entrada de la ejecución está en
[`generated/main.py`](./generated/main.py).

| Archivo | Responsabilidad |
|---|---|
| [`semantics/listener.py`](./semantics/listener.py) | Conecta el árbol de ANTLR con los puntos neurálgicos. |
| [`semantics/analizador.py`](./semantics/analizador.py) | Tablas: directorio, variables, ámbito actual y errores semánticos. |
| [`semantics/generador.py`](./semantics/generador.py) | Pilas y generación de cuádruplos. |
| [`semantics/memoria_virtual.py`](./semantics/memoria_virtual.py) | Reparte direcciones virtuales (compilación). |
| [`semantics/maquina_virtual.py`](./semantics/maquina_virtual.py) | Ejecuta los cuádruplos (memoria de ejecución). |
| [`semantics/directorio_funciones.py`](./semantics/directorio_funciones.py), [`tabla_variables.py`](./semantics/tabla_variables.py), [`cubo_semantico.py`](./semantics/cubo_semantico.py), [`cuadruplo.py`](./semantics/cuadruplo.py), [`pila.py`](./semantics/pila.py) | Estructuras de datos. |

### 4. Estructuras semánticas

- **Directorio de funciones:** registra cada función, su tipo de retorno, sus
  parámetros en orden y su tabla de variables. El programa también se registra
  como una entrada; su tabla representa el ámbito global.
- **Tabla de variables:** guarda el tipo de cada variable dentro de un ámbito.
  Una variable local o un parámetro no puede tener el mismo nombre que una
  variable global.
- **Cubo semántico:** recibe los tipos de dos operandos y un operador. Devuelve
  el tipo resultante o `None` si la operación no es válida.
- **Pilas del generador:**
  - `pila_operandos`: objetos `Operando` (nombre, tipo y dirección juntos).
  - `pila_operadores`: operadores pendientes y el fondo falso `(`.
  - `pila_saltos`: números de cuádruplos que se rellenan después (`GOTOF`,
    `GOTO` pendientes y el inicio de cada `while`). Al ser una sola pila, los
    `if` y `while` anidados se resuelven en el orden correcto.
  - `pila_llamadas`: llamadas a función abiertas (ya se generó su `ERA`).
- **Fila de cuádruplos:** conserva las instrucciones en el orden en que se
  generan.

### 5. Validaciones semánticas actuales

El analizador reporta:

1. Variables doblemente declaradas en el mismo ámbito.
2. Funciones doblemente declaradas.
3. Parámetros repetidos.
4. Variables no declaradas.
5. Funciones no declaradas.
6. Búsqueda de variables primero en el ámbito local y luego en el global.
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
validaciones, la generación de cuádruplos (expresiones, estatutos, control y
funciones), la memoria virtual y la ejecución en la máquina virtual.

## Direcciones virtuales

Cada variable, constante y temporal recibe una dirección fija dentro de un
segmento. Las direcciones permiten que los cuádruplos se ejecuten sin depender
del nombre original de los identificadores.

| Segmento | `int` | `float` | `bool` | `string` |
|---|---:|---:|---:|---:|
| Global | 1000-1999 | 2000-2999 | 3000-3999 | No aplica |
| Local | 4000-4999 | 5000-5999 | 6000-6999 | No aplica |
| Temporal | 7000-7999 | 8000-8999 | 9000-9999 | No aplica |
| Constante | 10000-10999 | 11000-11999 | 12000-12999 | 13000-13999 |

Los strings solo aparecen como letreros de `print`, por eso solo existen como
constantes.

Cada segmento mantiene un contador independiente. Los contadores **locales y
temporales se reinician** al empezar cada función y al empezar `main`: cada
función tiene su propio espacio, que en ejecución vive en su registro de
activación. Al terminar la función se guarda en el directorio cuántas
direcciones usó de cada tipo (`funcion.tamano`), que es lo que `ERA` reserva. `TablaVariables` guarda
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
exitExpresion (condición del if)
    -> agrega GOTOF(condición, -, ?) y mete su número a pila_saltos

enterElsep (si hay else)
    -> agrega GOTO(-, -, ?)
    -> saca el GOTOF de pila_saltos y lo rellena con el inicio del else
    -> mete el GOTO a pila_saltos

exitCondition
    -> saca el salto pendiente y lo rellena con la siguiente instrucción
```

Sin `else`, `GOTOF` se rellena al terminar el cuerpo. Los números del salto
son índices de instrucciones de la fila, no direcciones virtuales.

### `while ... do`

```text
enterCycle
    -> mete a pila_saltos la siguiente instrucción (inicio del ciclo)

exitExpresion (condición del while)
    -> agrega GOTOF(condición, -, ?) y mete su número a pila_saltos

exitCycle
    -> saca el GOTOF y luego el inicio
    -> agrega GOTO hacia el inicio
    -> rellena el GOTOF con la siguiente instrucción
```

### Declaración de función

```text
enterPrograma
    -> agrega (GOTO, -, -, ?) como cuádruplo 1: salto a main

enterFunc
    -> registra nombre y tipo de retorno
    -> reinicia los contadores locales y temporales
    -> si regresa int/float, reserva una variable GLOBAL para su retorno
    -> agrega parámetros con direcciones locales (en orden)
    -> guarda el número de cuádruplo donde empieza la función

exitDecl
    -> asigna direcciones locales a las variables de la función

exitReturnStmt
    -> valida el tipo contra el retorno de la función
    -> agrega (RETURN, valor, -, global_de_retorno)

exitFunc
    -> agrega ENDFUNC
    -> error si una función int/float no tiene ningún return
    -> guarda el tamaño: {"local": {tipo: n}, "temporal": {tipo: n}}
    -> restaura el ámbito global

enterBody (de main)
    -> rellena el GOTO main y reinicia los temporales

exitPrograma
    -> agrega END y guarda el tamaño global y el de main
```

### Invocación de función

```text
enterCall
    -> valida que la función exista
    -> agrega (ERA, -, -, función)
    -> guarda el tamaño de la pila de operandos

exitExpresion (argumentos)
    -> deja una dirección por cada argumento

exitCall
    -> valida número y tipos
    -> agrega (PARAM, argumento, -, parámetro) por argumento
    -> agrega (GOSUB, -, -, inicio de la función)
    -> si regresa valor: (=, global_de_retorno, -, temporal nuevo)
```

`ERA` no lleva el tamaño en el cuádruplo porque en una llamada recursiva la
función todavía no termina de compilarse; la máquina virtual lo lee del
directorio (`funcion.tamano`), que ya está completo al ejecutar.

El valor de retorno se deja en una variable global de la función (no en su
memoria local) porque el registro de activación se destruye al regresar. El
llamador lo copia de inmediato a un temporal propio, así que la recursión
(`n * fact(n - 1)`) no pierde valores.

Ejemplo (`tests/prueba.txt`, con `--virtual`):

```text
  1  (GOTO, -, -, 6)
  2  (*, 4000, 10000, 7000)      t = n * 2
  3  (=, 7000, -, 4001)
  4  (RETURN, 4001, -, 1002)     global de retorno de doble
  5  (ENDFUNC, -, -, -)
  6  (ERA, -, -, doble)
  7  (PARAM, 10001, -, 4000)     n = 3
  8  (GOSUB, -, -, 2)
  9  (=, 1002, -, 7000)
 10  (+, 7000, 10002, 7001)
 11  (=, 7001, -, 1000)
 12  (END, -, -, -)
```

### Códigos de operación

| Operador | Cuádruplo | Significado |
|---|---|---|
| `+ - * /` | `(op, izq, der, temp)` | Aritmética. `int / int` es división entera. |
| `> < !=` | `(op, izq, der, temp)` | Comparación; el resultado es `bool`. |
| `=` | `(=, valor, -, destino)` | Asignación (convierte `int` a `float` si el destino es float). |
| `PRINT` | `(PRINT, -, -, valor)` | Imprime una expresión o un letrero. |
| `READ` | `(READ, -, -, variable)` | Lee de la entrada y convierte al tipo de la variable. |
| `GOTO` | `(GOTO, -, -, n)` | Salta incondicionalmente al cuádruplo `n`. |
| `GOTOF` | `(GOTOF, cond, -, n)` | Si la condición es falsa, salta al cuádruplo `n`. |
| `ERA` | `(ERA, -, -, f)` | Crea el registro de activación de `f` con su tamaño. |
| `PARAM` | `(PARAM, arg, -, param)` | Copia el argumento al parámetro del registro nuevo. |
| `GOSUB` | `(GOSUB, -, -, n)` | Guarda el punto de regreso, activa el registro y salta. |
| `RETURN` | `(RETURN, valor, -, global)` | Guarda el valor en la global de retorno y regresa. |
| `ENDFUNC` | `(ENDFUNC, -, -, -)` | Fin de función: destruye el registro y regresa. |
| `END` | `(END, -, -, -)` | Fin del programa. |

## Máquina Virtual

La Máquina Virtual ([`semantics/maquina_virtual.py`](./semantics/maquina_virtual.py))
interpreta la fila de cuádruplos. El apuntador `ip` indica el cuádruplo actual;
avanza de uno en uno o cambia con `GOTO`, `GOTOF`, `GOSUB`, `RETURN` y
`ENDFUNC`. La ejecución empieza en el cuádruplo 1 (`GOTO main`) y termina con
`END`.

### Mapa de memoria de ejecución

```text
MemoriaEjecucion
├── globales     Segmento: int[] float[] bool[]      (vive todo el programa)
├── constantes   dict dirección -> valor              (solo lectura)
└── pila_registros
      ├── main   RegistroActivacion
      ├── f      RegistroActivacion
      └── ...    (tope = función que se está ejecutando)

RegistroActivacion
├── locales      Segmento: int[] float[] bool[]   (parámetros y variables)
├── temporales   Segmento: int[] float[] bool[]
├── funcion      entrada del directorio (inicio, retorno, tamaño)
└── ip_regreso   cuádruplo al que se vuelve
```

Cada `Segmento` tiene un arreglo por tipo del tamaño exacto que calculó el
compilador. Una dirección virtual se traduce a una celda así:

```text
dirección -> (segmento, tipo, desplazamiento) -> celda
1001      -> (global,   int,   1)             -> globales.int[1]
5002      -> (local,    float, 2)             -> tope.locales.float[2]
7000      -> (temporal, int,   0)             -> tope.temporales.int[0]
10003     -> (constante, int,  3)             -> constantes[10003]
```

Las direcciones locales y temporales siempre se resuelven en el registro del
tope de la pila, por eso dos llamadas a la misma función (por ejemplo en una
recursión) no comparten memoria.

### Estructuras auxiliares

| Estructura | Uso |
|---|---|
| `pila_registros` | Registros activos; `main` está en el fondo. |
| `registros_nuevos` | Pila de registros creados por `ERA` que esperan su `GOSUB`. Es pila porque un argumento puede contener otra llamada: `f(g(1))`. |
| `constantes` | Tabla dirección -> valor, cargada desde la tabla de constantes del compilador. |
| `ip` | Cuádruplo actual. |
| `salida` | Valores impresos (útil para las pruebas). |

### Flujo de una llamada

```text
ERA f      -> crea RegistroActivacion(f) con f.tamano y lo mete a registros_nuevos
PARAM a,p  -> lee a en el registro actual y lo escribe en p del registro nuevo
GOSUB      -> guarda ip_regreso = ip + 1, mete el registro a la pila y salta a f.inicio
RETURN v,g -> escribe v en la global de retorno g, saca el registro y vuelve a ip_regreso
ENDFUNC    -> saca el registro y vuelve a ip_regreso
```

### Errores de ejecución

- División entre cero.
- Uso de una variable que no tiene valor asignado.
- Una función `int`/`float` llega a `ENDFUNC` sin ejecutar `return`.
- Desbordamiento de pila (más de 1000 llamadas anidadas).
- Entrada de `read` que no corresponde al tipo de la variable.
