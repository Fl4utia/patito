"""
Puntos neuralgicos de BabyDuck.

AnalizadorSemantico: puntos neuralgicos de las tablas (directorio y variables).
GeneradorCuadruplos: puntos neuralgicos de las expresiones y estatutos lineales.
ListenerSemantico: listener de ANTLR que conecta el arbol de Lang.g4 con el analizador.

ANTLR llama a enterX al entrar a la regla X y a exitX al salir de ella.
Requiere haber generado LangListener.py con:  antlr4 -Dlanguage=Python3 Lang.g4
"""
try:
    from generated.LangListener import LangListener
except ImportError: # permite probar el analizador sin haber generado el codigo de ANTLR
    LangListener = object

from .cubo_semantico import CuboSemantico
from .directorio_funciones import DirectorioFunciones, Funcion
from .cuadruplo import FilaCuadruplos
from .stack import Stack
from .memoria_virtual import MemoriaVirtual


class AnalizadorSemantico:
    """
    Decisiones de diseno :
      - Una variable local o un parametro PUEDE llamarse igual que una global
        (la local oculta a la global). Solo se rechaza el nombre repetido dentro
        del MISMO ambito.
      - Los errores se acumulan en self.errores y el analisis continua.
    """

    def __init__(self):
        self.directorio = None
        self.ambito = None # Funcion en la que se esta (programa o funcion)
        self.errores = []
        self.memoria = MemoriaVirtual()

    def error(self, linea, mensaje):
        self.errores.append(f"línea {linea}: {mensaje}")

    # Punto neuralgico 1: al entrar al programa
    def inicio_programa(self, nombre):
        self.directorio = DirectorioFunciones(nombre, self.memoria)
        self.ambito = self.directorio.obtener_funcion(nombre)

    # Punto neuralgico 2: al terminar una declaracion "ids : tipo ;"
    def declarar_variables(self, nombres, tipo, linea):
        for nombre in nombres:
            if not self.ambito.variables.agregar(nombre, tipo):
                self.error(linea, f"variable '{nombre}' doblemente declarada")

    # Punto neuralgico 3: al entrar a una funcion (despues de leer tipo e id)
    def inicio_funcion(self, nombre, retorno, linea):
        funcion = self.directorio.agregar_funcion(nombre, retorno)
        if funcion is None:
            self.error(linea, f"función '{nombre}' doblemente declarada")
            # Se analiza su cuerpo en una funcion desechable para no ensuciar el directorio
            funcion = Funcion(nombre, retorno)
        if retorno in ("int", "float"):
            funcion.retorno_address = self.memoria.asignar_temporal(retorno)
        self.ambito = funcion

    # Punto neuralgico 4: por cada parametro "id : tipo"
    def agregar_parametro(self, nombre, tipo, linea):
        if not self.directorio.agregar_parametro(self.ambito, nombre, tipo):
            self.error(linea, f"parámetro '{nombre}' repetido en la función '{self.ambito.nombre}'")

    # Punto neuralgico 5: al salir de una funcion
    def fin_funcion(self):
        self.ambito = self.directorio.obtener_funcion(self.directorio.nombre_programa)

    # Punto neuralgico 6: al usar una variable (asignacion, read, factor)
    def usar_variable(self, nombre, linea):
        info = self.directorio.buscar_variable(nombre, self.ambito)
        if info is None:
            self.error(linea, f"variable '{nombre}' no declarada")
            return None
        return info["tipo"]

    def usar_variable_info(self, nombre, linea):
        info = self.directorio.buscar_variable(nombre, self.ambito)
        if info is None:
            self.error(linea, f"variable '{nombre}' no declarada")
            return None
        return info

    # Punto neuralgico 7: al llamar una funcion
    def llamar_funcion(self, nombre, linea):
        funcion = self.directorio.obtener_funcion(nombre)
        if funcion is None or nombre == self.directorio.nombre_programa:
            self.error(linea, f"función '{nombre}' no declarada")
            return None
        return funcion


class GeneradorCuadruplos:
    """
    Puntos neuralgicos que traducen expresiones y estatutos lineales a cuadruplos.

    Estructuras:
        pila_operandos:  nombres, constantes y temporales   (ej. 'a', '5', 't1')
        pila_tipos:      el tipo de cada operando, en paralelo ('int', 'float', 'bool')
        pila_operadores: operadores pendientes y el fondo falso '('
        fila:            FilaCuadruplos con el resultado

    Idea: el arbol de ANTLR ya trae la precedencia y la asociatividad (el '*' queda
    mas adentro que el '+', y 'a - b - c' se agrupa como '(a - b) - c'). Por eso
    cada nodo con operador funciona asi:
        1. al ENTRAR al nodo se apila su operador;
        2. los hijos se procesan y dejan sus operandos en la pila;
        3. al SALIR del nodo se reduce: se sacan 2 operandos y el operador,
           se consulta el cubo y se genera el cuadruplo.

    El cubo devuelve None cuando la combinacion no es valida. Cuando un operando
    tiene tipo 'error' (marca propia de esta clase: variable no declarada, tipos
    incompatibles) se sigue propagando 'error' sin generar cuadruplos, para
    no llenar de errores en cadena.
    """

    def __init__(self, analizador):
        self.analizador = analizador       # para reportar errores y buscar variables
        self.cubo = CuboSemantico()
        self.pila_operandos = Stack()
        self.pila_tipos = Stack()
        self.pila_direcciones = Stack()
        self.pila_operadores = Stack()
        self.pila_saltos = []
        self.pila_condiciones = []
        self.pila_ciclos = []
        self.fila = FilaCuadruplos()
        self.contador_temporales = 0       # para nombrar t1, t2, t3...
        self.tamanos_llamada = []          # tamano de la pila de operandos al abrir cada llamada
        self.pila_resultados_llamadas = []
        self.ultimo_temporal = None

    # ---------- Apoyo ----------
    def nuevo_temporal(self, tipo="int"):
        """Crea el siguiente nombre y direccion temporal."""
        self.contador_temporales = self.contador_temporales + 1
        nombre = "t" + str(self.contador_temporales)
        direccion = self.analizador.memoria.asignar_temporal(tipo)
        self.ultimo_temporal = (nombre, direccion)
        return nombre

    def meter_operando(self, nombre, tipo, direccion=None):
        """Apila un operando y su tipo (siempre van juntos)."""
        if direccion is None:
            if tipo == "error":
                direccion = None
            elif nombre.startswith("t") and tipo in ("int", "float", "bool"):
                direccion = self.ultimo_temporal[1] if self.ultimo_temporal else None
            elif tipo in ("int", "float", "string"):
                direccion = self.analizador.memoria.asignar_constante(nombre, tipo)
        self.pila_operandos.push(nombre)
        self.pila_tipos.push(tipo)
        self.pila_direcciones.push(direccion)

    def sacar_operando(self):
        """Saca el operando del tope y su tipo. Devuelve (nombre, tipo)."""
        nombre = self.pila_operandos.pop()
        tipo = self.pila_tipos.pop()
        direccion = self.pila_direcciones.pop()
        self.ultima_direccion = direccion
        return nombre, tipo

    # Punto neuralgico 8: llega un ID o una constante
    def operando_variable(self, nombre, linea):
        info = self.analizador.usar_variable_info(nombre, linea)
        if info is None:
            self.meter_operando(nombre, "error", None)
        else:
            self.meter_operando(nombre, info["tipo"], info["address"])

    def operando_constante(self, texto, tipo):
        direccion = self.analizador.memoria.asignar_constante(texto, tipo)
        self.meter_operando(texto, tipo, direccion)

    # Punto neuralgico 9: llega un operador (+ - * / > < !=)
    def meter_operador(self, operador):
        self.pila_operadores.push(operador)

    # Punto neuralgico 10: fondo falso para '( expresion )'
    def abrir_parentesis(self):
        self.pila_operadores.push("(")

    def cerrar_parentesis(self):
        self.pila_operadores.pop()         # quita el '('

    # Punto neuralgico 11: reducir (se terminaron los dos operandos de un operador)
    def reducir(self, linea):
        operador = self.pila_operadores.pop()
        der, tipo_der = self.sacar_operando()
        direccion_der = self.ultima_direccion
        izq, tipo_izq = self.sacar_operando()
        direccion_izq = self.ultima_direccion

        if tipo_izq == "error" or tipo_der == "error":
            self.meter_operando("error", "error")      # el error ya se reporto antes
            return

        tipo_resultado = self.cubo.resultado(tipo_izq, tipo_der, operador)
        if tipo_resultado is None:            # el cubo devuelve None si no es valido
            self.analizador.error(
                linea, f"tipos incompatibles: {tipo_izq} {operador} {tipo_der}")
            self.meter_operando("error", "error")
            return

        temporal = self.nuevo_temporal(tipo_resultado)
        direccion_temporal = self.ultimo_temporal[1]
        self.fila.agregar(
            operador, izq, der, temporal,
            direccion_izq, direccion_der, direccion_temporal,
        )
        self.meter_operando(temporal, tipo_resultado, direccion_temporal)

    # Punto neuralgico 12: menos unario (-x se traduce como 0 - x)
    def negar(self, linea):
        x, tipo_x = self.sacar_operando()
        direccion_x = self.ultima_direccion
        direccion_cero = self.analizador.memoria.asignar_constante("0", "int")
        self.meter_operando("0", "int", direccion_cero)
        self.meter_operando(x, tipo_x, direccion_x)
        self.pila_operadores.push("-")
        self.reducir(linea)

    # Punto neuralgico 13: asignacion  ID = expresion ;
    def asignar(self, nombre, linea):
        valor, tipo_valor = self.sacar_operando()
        direccion_valor = self.ultima_direccion
        info_variable = self.analizador.usar_variable_info(nombre, linea)

        if info_variable is None or tipo_valor == "error":
            return                                      # ya hay un error reportado

        tipo_variable = info_variable["tipo"]
        if self.cubo.resultado(tipo_variable, tipo_valor, "=") is None:
            self.analizador.error(
                linea, f"no se puede asignar {tipo_valor} a '{nombre}' ({tipo_variable})")
            return
        self.fila.agregar(
            "=", valor, None, nombre,
            direccion_valor, None, info_variable["address"],
        )

    # Punto neuralgico 14: print de una expresion o de un letrero
    def imprimir_expresion(self):
        valor, tipo = self.sacar_operando()
        direccion = self.ultima_direccion
        if tipo != "error":
            self.fila.agregar("PRINT", None, None, valor, None, None, direccion)

    def imprimir_letrero(self, texto):
        direccion = self.analizador.memoria.asignar_constante(texto, "string")
        self.fila.agregar("PRINT", None, None, texto, None, None, direccion)

    # Punto neuralgico 15: read(ID)
    def leer(self, nombre, linea):
        info = self.analizador.usar_variable_info(nombre, linea)
        if info is not None:
            self.fila.agregar("READ", None, None, nombre, None, None, info["address"])

    # Punto neuralgico 16: return expresion
    def regresar(self, linea):
        valor, tipo = self.sacar_operando()
        direccion_valor = self.ultima_direccion
        if tipo == "error":
            return
        retorno = self.analizador.ambito.retorno
        if retorno is None or retorno == "void":
            self.analizador.error(linea, "return no puede regresar un valor aqui")
            return
        if self.cubo.resultado(retorno, tipo, "=") is None:
            self.analizador.error(
                linea, f"return de tipo {tipo} en una función que regresa {retorno}")
            return
        direccion_retorno = self.analizador.ambito.retorno_address
        self.fila.agregar(
            "RETURN", valor, None, "retorno",
            direccion_valor, None, direccion_retorno,
        )

    # Punto neuralgico 17: la expresion de un if o while ya se evaluo.
    def iniciar_if(self):
        self.pila_condiciones.append({"gotof": None, "goto": None})

    def iniciar_ciclo(self):
        self.pila_ciclos.append({"inicio": self.fila.siguiente(), "gotof": None})

    def terminar_expresion_control(self, linea):
        condicion, tipo = self.sacar_operando()
        direccion = self.ultima_direccion
        if tipo != "bool" and tipo != "error":
            self.analizador.error(linea, "la condicion debe producir bool")
            tipo = "error"
        if tipo == "error":
            return
        numero = self.fila.agregar(
            "GOTOF", condicion, None, None,
            direccion, None, None,
        )
        if self.pila_condiciones:
            self.pila_condiciones[-1]["gotof"] = numero
        if self.pila_ciclos:
            self.pila_ciclos[-1]["gotof"] = numero

    def entrar_else(self):
        if not self.pila_condiciones:
            return
        frame = self.pila_condiciones[-1]
        frame["goto"] = self.fila.agregar("GOTO", None, None, None)
        if frame["gotof"] is not None:
            self.fila.llenar(frame["gotof"], self.fila.siguiente())

    def cerrar_if(self):
        if not self.pila_condiciones:
            return
        frame = self.pila_condiciones.pop()
        if frame["goto"] is not None:
            self.fila.llenar(frame["goto"], self.fila.siguiente())
        elif frame["gotof"] is not None:
            self.fila.llenar(frame["gotof"], self.fila.siguiente())

    def cerrar_ciclo(self):
        if not self.pila_ciclos:
            return
        frame = self.pila_ciclos.pop()
        self.fila.agregar("GOTO", None, None, frame["inicio"])
        if frame["gotof"] is not None:
            self.fila.llenar(frame["gotof"], self.fila.siguiente())

    # Punto neuralgico 18: llamadas a funcion
    def abrir_llamada(self, nombre, linea):
        funcion = self.analizador.llamar_funcion(nombre, linea)
        self.tamanos_llamada.append({
            "nombre": nombre,
            "base": self.pila_operandos.tamano(),
            "funcion": funcion,
            "temporal": None,
        })
        self.fila.agregar("ERA", None, None, nombre)

    def cerrar_llamada(self, nombre, linea, usar_en_expresion=False):
        if not self.tamanos_llamada:
            return
        llamada = self.tamanos_llamada.pop()
        argumentos = []
        while self.pila_operandos.tamano() > llamada["base"]:
            argumento, tipo = self.sacar_operando()
            argumentos.append((argumento, tipo, self.ultima_direccion))
        argumentos.reverse()

        funcion = llamada["funcion"]
        if funcion is None:
            return
        parametros = funcion.parametros
        valido = len(argumentos) == len(parametros)
        if not valido:
            self.analizador.error(
                linea,
                f"la función '{nombre}' espera {len(parametros)} argumentos "
                f"y recibió {len(argumentos)}",
            )
        else:
            for (argumento, tipo, direccion), (param_nombre, param_tipo) in zip(argumentos, parametros):
                if direccion is not None and self.cubo.resultado(param_tipo, tipo, "=") is None:
                    self.analizador.error(
                        linea,
                        f"tipo incompatible en parámetro '{param_nombre}' "
                        f"de '{nombre}'",
                    )
                    valido = False
        if not valido:
            return

        for (argumento, tipo, direccion), (param_nombre, param_tipo) in zip(argumentos, parametros):
            info_param = funcion.variables.obtener(param_nombre)
            direccion_param = info_param["address"] if info_param is not None else None
            self.fila.agregar(
                "PARAM", argumento, None, param_nombre,
                direccion, None, direccion_param,
            )

        inicio = funcion.inicio if funcion.inicio is not None else 0
        self.fila.agregar("GOSUB", None, None, nombre, None, None, inicio)
        if funcion.retorno != "void":
            temporal = self.nuevo_temporal(funcion.retorno)
            direccion_temporal = self.ultimo_temporal[1]
            llamada["temporal"] = (temporal, funcion.retorno, direccion_temporal)
            direccion_retorno = funcion.retorno_address
            self.fila.agregar(
                "=", nombre + "()", None, temporal,
                direccion_retorno, None, direccion_temporal,
            )
            if usar_en_expresion:
                self.pila_resultados_llamadas.append(llamada["temporal"])

    def resultado_llamada(self, nombre, linea):
        """Una llamada dentro de una expresion: apila su temporal de retorno."""
        funcion = self.analizador.directorio.obtener_funcion(nombre)
        if funcion is None or nombre == self.analizador.directorio.nombre_programa:
            self.meter_operando("error", "error")
        elif funcion.retorno == "void":
            self.analizador.error(linea, f"la función void '{nombre}' no regresa valor")
            self.meter_operando("error", "error")
        elif self.pila_resultados_llamadas:
            temporal, tipo, direccion = self.pila_resultados_llamadas.pop()
            self.meter_operando(temporal, tipo, direccion)


class ListenerSemantico(LangListener):
    def __init__(self):
        super().__init__()
        self.analizador = AnalizadorSemantico()
        self.generador = None              # se crea al entrar al programa

    # programa: PROGRAM ID SEMI vars funcs MAIN body END EOF
    def enterPrograma(self, ctx):
        self.analizador.inicio_programa(ctx.ID().getText())
        self.generador = GeneradorCuadruplos(self.analizador)
        programa = self.analizador.directorio.obtener_funcion(ctx.ID().getText())
        programa.inicio = None

    def enterBody(self, ctx):
        if type(ctx.parentCtx).__name__ == "ProgramaContext":
            programa = self.analizador.directorio.obtener_funcion(
                self.analizador.directorio.nombre_programa
            )
            if programa.inicio is None:
                programa.inicio = self.generador.fila.siguiente()

    # decl: ids COLON tipo SEMI      (ids es recursiva: ID | ID COMMA ids)
    def exitDecl(self, ctx):
        nombres = []
        ids = ctx.ids()
        while ids is not None:
            nombres.append(ids.ID().getText())
            ids = ids.ids()
        self.analizador.declarar_variables(nombres, ctx.tipo().getText(), ctx.start.line)

    # func: rtype ID LPAREN params RPAREN LBRACK vars body RBRACK SEMI
    def enterFunc(self, ctx):
        self.analizador.inicio_funcion(ctx.ID().getText(), ctx.rtype().getText(), ctx.start.line)
        funcion = self.analizador.ambito
        funcion.inicio = self.generador.fila.siguiente()
        # params: plist | epsilon ;  plist es recursiva: ID COLON tipo (COMMA plist)?
        plist = ctx.params().plist()
        while plist is not None:
            self.analizador.agregar_parametro(
                plist.ID().getText(), plist.tipo().getText(), plist.start.line
            )
            plist = plist.plist()

    def exitFunc(self, ctx):
        self.generador.fila.agregar("ENDFUNC", None, None, None)
        self.analizador.fin_funcion()

    # ---------- Estatutos lineales ----------
    # assign: ID ASSIGN expresion SEMI     (al salir, el valor ya esta en la pila)
    def exitAssign(self, ctx):
        self.generador.asignar(ctx.ID().getText(), ctx.start.line)

    # readStmt: READ LPAREN ID RPAREN SEMI
    def exitReadStmt(self, ctx):
        self.generador.leer(ctx.ID().getText(), ctx.start.line)

    # returnStmt: RETURN expresion SEMI
    def exitReturnStmt(self, ctx):
        self.generador.regresar(ctx.start.line)

    # parg: expresion | CTE_STRING        (print(a + 1, "hola"))
    def exitParg(self, ctx):
        if ctx.CTE_STRING() is not None:
            self.generador.imprimir_letrero(ctx.CTE_STRING().getText())
        else:
            self.generador.imprimir_expresion()

    # condition: IF LPAREN expresion RPAREN body elsep SEMI
    def enterCondition(self, ctx):
        self.generador.iniciar_if()

    def exitCondition(self, ctx):
        self.generador.cerrar_if()

    # cycle: WHILE LPAREN expresion RPAREN DO body SEMI
    def enterCycle(self, ctx):
        self.generador.iniciar_ciclo()

    def exitCycle(self, ctx):
        self.generador.cerrar_ciclo()

    # elsep: ELSE body |
    def enterElsep(self, ctx):
        if ctx.ELSE() is not None:
            self.generador.entrar_else()

    # ---------- Expresiones ----------
    # expresion: exp | exp rel exp
    def enterExpresion(self, ctx):
        if ctx.rel() is not None:
            self.generador.meter_operador(ctx.rel().getText())

    def exitExpresion(self, ctx):
        if ctx.rel() is not None:
            self.generador.reducir(ctx.start.line)
        parent_name = type(ctx.parentCtx).__name__
        if parent_name in ("ConditionContext", "CycleContext"):
            self.generador.terminar_expresion_control(ctx.start.line)

    # exp: termino | exp PLUS termino | exp MINUS termino
    def enterExp(self, ctx):
        if ctx.PLUS() is not None:
            self.generador.meter_operador("+")
        if ctx.MINUS() is not None:
            self.generador.meter_operador("-")

    def exitExp(self, ctx):
        if ctx.PLUS() is not None or ctx.MINUS() is not None:
            self.generador.reducir(ctx.start.line)

    # termino: factor | termino MULT factor | termino DIV factor
    def enterTermino(self, ctx):
        if ctx.MULT() is not None:
            self.generador.meter_operador("*")
        if ctx.DIV() is not None:
            self.generador.meter_operador("/")

    def exitTermino(self, ctx):
        if ctx.MULT() is not None or ctx.DIV() is not None:
            self.generador.reducir(ctx.start.line)

    # factor: LPAREN expresion RPAREN | call | ID | cte | sign ID | sign cte
    def enterFactor(self, ctx):
        if ctx.LPAREN() is not None:
            self.generador.abrir_parentesis()

    def exitFactor(self, ctx):
        linea = ctx.start.line
        if ctx.LPAREN() is not None:
            self.generador.cerrar_parentesis()
            return                               # el resultado ya esta en la pila

        if ctx.call() is not None:
            self.generador.resultado_llamada(ctx.call().ID().getText(), linea)
            return

        if ctx.ID() is not None:
            self.generador.operando_variable(ctx.ID().getText(), linea)
        else:
            cte = ctx.cte()
            if cte.CTE_INT() is not None:
                self.generador.operando_constante(cte.getText(), "int")
            else:
                self.generador.operando_constante(cte.getText(), "float")

        # Signo unario: '+x' no cambia nada, '-x' se traduce como 0 - x
        if ctx.sign() is not None and ctx.sign().MINUS() is not None:
            self.generador.negar(linea)

    # call: ID LPAREN args RPAREN     (se usa en fCall y dentro de factor)
    def enterCall(self, ctx):
        self.generador.abrir_llamada(ctx.ID().getText(), ctx.start.line)

    def exitCall(self, ctx):
        usar_en_expresion = type(ctx.parentCtx).__name__ == "FactorContext"
        self.generador.cerrar_llamada(
            ctx.ID().getText(),
            ctx.start.line,
            usar_en_expresion,
        )