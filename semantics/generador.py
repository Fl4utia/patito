"""
Generador de cuadruplos de BabyDuck.

Traduce expresiones, estatutos, condiciones, ciclos y funciones a cuadruplos
con direcciones virtuales.

Estructuras:
    pila_operandos:  Operando (nombre + tipo + direccion) de cada valor pendiente
    pila_operadores: operadores pendientes ('+', '*', ...) y el fondo falso '('
    pila_saltos:     numeros de cuadruplos que hay que rellenar despues
                     (GOTOF / GOTO pendientes y el inicio de cada while)
    pila_llamadas:   llamadas a funcion abiertas (ya se genero su ERA)
    fila:            FilaCuadruplos con el resultado

Idea de las expresiones: el arbol de ANTLR ya trae la precedencia y la
asociatividad (el '*' queda mas adentro que el '+'). Por eso cada nodo con
operador funciona asi:
    1. al ENTRAR al nodo se apila su operador;
    2. los hijos se procesan y dejan sus operandos en la pila;
    3. al SALIR del nodo se reduce: se sacan 2 operandos y el operador,
       se consulta el cubo y se genera el cuadruplo.

Errores: cuando algo falla (variable no declarada, tipos incompatibles) se
apila un operando de tipo 'error'. Quien lo recibe ya no genera cuadruplos ni
vuelve a reportar, para no llenar la salida de errores en cadena.
"""
from .cubo_semantico import CuboSemantico
from .cuadruplo import FilaCuadruplos
from .pila import Pila


class Operando:
    """Un valor en la pila de operandos."""

    def __init__(self, nombre, tipo, direccion):
        self.nombre = nombre          # como se ve en el codigo: 'a', '5', 't1'
        self.tipo = tipo              # 'int', 'float', 'bool', 'string' o 'error'
        self.direccion = direccion    # direccion virtual (None si es error)

    def es_error(self):
        return self.tipo == "error"


def operando_error():
    """Operando que marca que la expresion ya tuvo un error reportado."""
    return Operando("error", "error", None)


class GeneradorCuadruplos:
    def __init__(self, analizador):
        """
        Args:
            analizador (AnalizadorSemantico): para buscar variables y funciones,
                pedir direcciones y reportar errores.
        """
        self.analizador = analizador
        self.memoria = analizador.memoria
        self.cubo = CuboSemantico()
        self.fila = FilaCuadruplos()

        self.pila_operandos = Pila()
        self.pila_operadores = Pila()
        self.pila_saltos = Pila()
        self.pila_llamadas = Pila()

        self.contador_temporales = 0     # para nombrar t1, t2, t3...
        self.goto_main = None            # numero del cuadruplo (GOTO, -, -, main)

    # ------------------------------------------------------------------
    # Apoyo
    # ------------------------------------------------------------------
    def nuevo_temporal(self, tipo):
        """
        Crea un temporal: un nombre (t1, t2...) y una direccion del segmento temporal.

        Returns:
            Operando del temporal.
        """
        self.contador_temporales += 1
        nombre = f"t{self.contador_temporales}"
        direccion = self.memoria.asignar_temporal(tipo)
        return Operando(nombre, tipo, direccion)

    def generar(self, operador, izquierdo=None, derecho=None, resultado=None):
        """
        Agrega un cuadruplo a partir de Operandos (o None).
        Copia por separado los nombres y las direcciones de cada operando.

        Returns:
            int: numero del cuadruplo generado.
        """
        return self.fila.agregar(
            operador,
            izquierdo.nombre if izquierdo else None,
            derecho.nombre if derecho else None,
            resultado.nombre if resultado else None,
            izquierdo.direccion if izquierdo else None,
            derecho.direccion if derecho else None,
            resultado.direccion if resultado else None,
        )

    def generar_salto(self, operador, condicion=None, destino=None):
        """
        Agrega GOTO o GOTOF. El destino es un NUMERO de cuadruplo (no una direccion);
        si aun no se conoce se deja en None y se rellena despues.
        """
        return self.fila.agregar(
            operador,
            condicion.nombre if condicion else None, None, destino,
            condicion.direccion if condicion else None, None, destino,
        )

    # ------------------------------------------------------------------
    # Programa
    # ------------------------------------------------------------------
    def iniciar_programa(self):
        """Cuadruplo 1: salto a main. El destino se rellena al llegar a main."""
        self.goto_main = self.generar_salto("GOTO")

    def iniciar_main(self):
        """
        Rellena el GOTO del cuadruplo 1 con el inicio de main.

        Returns:
            int: numero del primer cuadruplo de main.
        """
        inicio = self.fila.siguiente()
        self.fila.llenar(self.goto_main, inicio)
        return inicio

    def terminar_programa(self):
        self.generar("END")

    # ------------------------------------------------------------------
    # Operandos y operadores
    # ------------------------------------------------------------------
    def operando_variable(self, nombre, linea):
        """Llega un ID dentro de una expresion: se apila con su tipo y direccion."""
        info = self.analizador.buscar_variable(nombre, linea)
        if info is None:
            self.pila_operandos.meter(operando_error())
        else:
            self.pila_operandos.meter(Operando(nombre, info["tipo"], info["address"]))

    def operando_constante(self, texto, tipo):
        """Llega una constante (5, 2.5): se apila con su direccion de constante."""
        direccion = self.memoria.asignar_constante(texto, tipo)
        self.pila_operandos.meter(Operando(texto, tipo, direccion))

    def meter_operador(self, operador):
        self.pila_operadores.meter(operador)

    def abrir_parentesis(self):
        """'(' funciona como fondo falso de la pila de operadores."""
        self.pila_operadores.meter("(")

    def cerrar_parentesis(self):
        self.pila_operadores.sacar()

    # ------------------------------------------------------------------
    # Expresiones
    # ------------------------------------------------------------------
    def reducir(self, linea):
        """
        Ya estan los dos operandos de un operador: genera  (op, izq, der, temporal).
        """
        operador = self.pila_operadores.sacar()
        derecho = self.pila_operandos.sacar()       # el derecho esta arriba
        izquierdo = self.pila_operandos.sacar()

        # Si un operando ya trae error, solo se propaga (ya se reporto antes)
        if izquierdo.es_error() or derecho.es_error():
            self.pila_operandos.meter(operando_error())
            return

        # El cubo dice el tipo del resultado, o None si la operacion no es valida
        tipo_resultado = self.cubo.resultado(izquierdo.tipo, derecho.tipo, operador)
        if tipo_resultado is None:
            self.analizador.error(
                linea, f"tipos incompatibles: {izquierdo.tipo} {operador} {derecho.tipo}")
            self.pila_operandos.meter(operando_error())
            return

        temporal = self.nuevo_temporal(tipo_resultado)
        self.generar(operador, izquierdo, derecho, temporal)
        self.pila_operandos.meter(temporal)

    def negar(self, linea):
        """Menos unario:  -x  se traduce como  0 - x."""
        x = self.pila_operandos.sacar()
        self.operando_constante("0", "int")
        self.pila_operandos.meter(x)
        self.pila_operadores.meter("-")
        self.reducir(linea)

    # ------------------------------------------------------------------
    # Estatutos lineales
    # ------------------------------------------------------------------
    def asignar(self, nombre, linea):
        """ID = expresion ;   ->   (=, valor, -, variable)"""
        valor = self.pila_operandos.sacar()
        info = self.analizador.buscar_variable(nombre, linea)
        if info is None or valor.es_error():
            return

        variable = Operando(nombre, info["tipo"], info["address"])
        if self.cubo.resultado(variable.tipo, valor.tipo, "=") is None:
            self.analizador.error(
                linea, f"no se puede asignar {valor.tipo} a '{nombre}' ({variable.tipo})")
            return

        self.generar("=", valor, None, variable)

    def imprimir_expresion(self):
        """print(expresion)   ->   (PRINT, -, -, valor)"""
        valor = self.pila_operandos.sacar()
        if not valor.es_error():
            self.generar("PRINT", resultado=valor)

    def imprimir_letrero(self, texto):
        """print("letrero")   ->   (PRINT, -, -, "letrero")"""
        direccion = self.memoria.asignar_constante(texto, "string")
        self.generar("PRINT", resultado=Operando(texto, "string", direccion))

    def leer(self, nombre, linea):
        """read(ID)   ->   (READ, -, -, variable)"""
        info = self.analizador.buscar_variable(nombre, linea)
        if info is not None:
            self.generar("READ", resultado=Operando(nombre, info["tipo"], info["address"]))

    def regresar(self, linea):
        """return expresion ;   ->   (RETURN, valor, -, global_de_retorno)"""
        valor = self.pila_operandos.sacar()
        funcion = self.analizador.ambito
        funcion.tiene_return = True
        if valor.es_error():
            return

        if not funcion.regresa_valor():
            self.analizador.error(linea, "return no puede regresar un valor aqui")
            return
        if self.cubo.resultado(funcion.retorno, valor.tipo, "=") is None:
            self.analizador.error(
                linea, f"return de tipo {valor.tipo} en una función que regresa {funcion.retorno}")
            return

        destino = Operando(funcion.nombre, funcion.retorno, funcion.retorno_address)
        self.generar("RETURN", valor, None, destino)

    # ------------------------------------------------------------------
    # Estatutos de control (pila de saltos)
    # ------------------------------------------------------------------
    #   if (c) { A } else { B };          while (c) do { A };
    #
    #     c                                 inicio: c
    #     GOTOF c, -, ELSE                  GOTOF c, -, FIN
    #     A                                 A
    #     GOTO FIN                          GOTO inicio
    #   ELSE: B                           FIN:
    #   FIN:
    # ------------------------------------------------------------------
    def iniciar_ciclo(self):
        """Antes de la condicion del while: se guarda a donde hay que regresar."""
        self.pila_saltos.meter(self.fila.siguiente())

    def generar_gotof(self, linea):
        """La condicion de un if/while ya se evaluo: GOTOF con destino pendiente."""
        condicion = self.pila_operandos.sacar()
        if not condicion.es_error() and condicion.tipo != "bool":
            self.analizador.error(linea, "la condicion debe producir bool")

        # Se genera aunque haya error, para que la pila de saltos quede pareja.
        # (Un programa con errores nunca se ejecuta.)
        gotof = self.generar_salto("GOTOF", condicion)
        self.pila_saltos.meter(gotof)

    def iniciar_else(self):
        """Fin del bloque 'then': salto al final y el GOTOF apunta al else."""
        goto_fin = self.generar_salto("GOTO")
        gotof = self.pila_saltos.sacar()
        self.fila.llenar(gotof, self.fila.siguiente())
        self.pila_saltos.meter(goto_fin)

    def cerrar_if(self):
        """El salto pendiente (GOTOF sin else, o GOTO con else) apunta aqui."""
        pendiente = self.pila_saltos.sacar()
        self.fila.llenar(pendiente, self.fila.siguiente())

    def cerrar_ciclo(self):
        """GOTO de regreso a la condicion, y el GOTOF apunta a la salida."""
        gotof = self.pila_saltos.sacar()
        inicio = self.pila_saltos.sacar()
        self.generar_salto("GOTO", destino=inicio)
        self.fila.llenar(gotof, self.fila.siguiente())

    # ------------------------------------------------------------------
    # Funciones
    # ------------------------------------------------------------------
    def terminar_funcion(self):
        self.generar("ENDFUNC")

    def abrir_llamada(self, nombre, linea):
        """
        Inicio de una llamada  f( ... ):  valida que f exista y genera ERA.

        Se guarda cuantos operandos habia en la pila: todo lo que se apile
        encima, hasta cerrar la llamada, son los argumentos.
        """
        funcion = self.analizador.llamar_funcion(nombre, linea)
        self.pila_llamadas.meter({
            "funcion": funcion,
            "operandos_antes": self.pila_operandos.tamano(),
        })
        # El tamano no va en el cuadruplo: en una llamada recursiva todavia no se
        # conoce. La maquina virtual lo busca en el directorio (funcion.tamano).
        self.generar("ERA", resultado=Operando(nombre, None, None))

    def cerrar_llamada(self, nombre, linea, en_expresion):
        """
        Fin de una llamada: valida argumentos y genera PARAM, GOSUB y la copia del retorno.

        Args:
            nombre (str): nombre de la funcion.
            linea (int): para reportar errores.
            en_expresion (bool): True si la llamada esta dentro de una expresion
                (ej. a = f(1) + 2). Entonces su resultado se apila como operando.
        """
        llamada = self.pila_llamadas.sacar()
        funcion = llamada["funcion"]
        argumentos = self._sacar_argumentos(llamada["operandos_antes"])

        resultado = self._generar_llamada(funcion, nombre, argumentos, linea)

        # Dentro de una expresion la llamada deja SIEMPRE un operando
        # (su temporal, o 'error'), para que la expresion siga cuadrando.
        if en_expresion:
            if funcion is not None and not funcion.regresa_valor():
                self.analizador.error(linea, f"la función void '{nombre}' no regresa valor")
            if resultado is None:
                resultado = operando_error()
            self.pila_operandos.meter(resultado)

    def _sacar_argumentos(self, operandos_antes):
        """Saca los argumentos de la pila y los regresa en el orden en que se escribieron."""
        argumentos = []
        while self.pila_operandos.tamano() > operandos_antes:
            argumentos.append(self.pila_operandos.sacar())
        argumentos.reverse()
        return argumentos

    def _generar_llamada(self, funcion, nombre, argumentos, linea):
        """
        Valida y genera los cuadruplos de la llamada.

        Returns:
            Operando con el temporal del valor de retorno, o None si la funcion
            es void o hubo un error.
        """
        if funcion is None:                                    # ya se reporto
            return None
        if any(argumento.es_error() for argumento in argumentos):
            return None

        # 1. Mismo numero de argumentos que de parametros
        if len(argumentos) != len(funcion.parametros):
            self.analizador.error(
                linea,
                f"la función '{nombre}' espera {len(funcion.parametros)} argumentos "
                f"y recibió {len(argumentos)}",
            )
            return None

        # 2. Cada argumento compatible con su parametro (como una asignacion)
        for argumento, (param_nombre, param_tipo) in zip(argumentos, funcion.parametros):
            if self.cubo.resultado(param_tipo, argumento.tipo, "=") is None:
                self.analizador.error(
                    linea, f"tipo incompatible en parámetro '{param_nombre}' de '{nombre}'")
                return None

        # 3. PARAM por cada argumento: (PARAM, argumento, -, parametro)
        for argumento, (param_nombre, param_tipo) in zip(argumentos, funcion.parametros):
            info = funcion.variables.obtener(param_nombre)
            parametro = Operando(param_nombre, param_tipo, info["address"])
            self.generar("PARAM", argumento, None, parametro)

        # 4. GOSUB al inicio de la funcion
        self.fila.agregar("GOSUB", None, None, nombre, None, None, funcion.inicio)

        # 5. Si regresa valor, se copia de su global de retorno a un temporal propio
        if not funcion.regresa_valor():
            return None
        global_retorno = Operando(nombre, funcion.retorno, funcion.retorno_address)
        temporal = self.nuevo_temporal(funcion.retorno)
        self.generar("=", global_retorno, None, temporal)
        return temporal
