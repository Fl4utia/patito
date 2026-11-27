"""
Listener de ANTLR: conecta el arbol de Lang.g4 con los puntos neuralgicos.

ANTLR recorre el arbol y llama a enterX al entrar a la regla X y a exitX al
salir de ella. Este archivo NO tiene logica propia: solo decide en que momento
llamar al analizador (tablas) y al generador (cuadruplos).

    AnalizadorSemantico  -> directorio, tablas de variables, memoria, errores
    GeneradorCuadruplos  -> pilas y fila de cuadruplos

Requiere haber generado el parser con:
    antlr4 -Dlanguage=Python3 -o generated Lang.g4
"""
from generated.LangListener import LangListener
from generated.LangParser import LangParser

from .analizador import AnalizadorSemantico
from .generador import GeneradorCuadruplos


class ListenerSemantico(LangListener):
    def __init__(self):
        super().__init__()
        self.analizador = AnalizadorSemantico()
        self.generador = None              # se crea al entrar al programa

    # ------------------------------------------------------------------
    # Programa
    # programa: PROGRAM ID SEMI vars funcs MAIN body END EOF
    # ------------------------------------------------------------------
    def enterPrograma(self, ctx):
        self.analizador.inicio_programa(ctx.ID().getText())
        self.generador = GeneradorCuadruplos(self.analizador)
        self.generador.iniciar_programa()                     # (GOTO, -, -, main)

    def exitPrograma(self, ctx):
        self.generador.terminar_programa()                    # (END, -, -, -)
        self.analizador.fin_programa()

    # body: LBRACE stmts RBRACE   (solo interesa el body de main)
    def enterBody(self, ctx):
        if isinstance(ctx.parentCtx, LangParser.ProgramaContext):
            programa = self.analizador.directorio.programa
            programa.inicio = self.generador.iniciar_main()
            self.analizador.inicio_main()

    # ------------------------------------------------------------------
    # Declaraciones
    # decl: ids COLON tipo SEMI        ids: ID | ID COMMA ids
    # ------------------------------------------------------------------
    def exitDecl(self, ctx):
        nombres = []
        ids = ctx.ids()
        while ids is not None:                 # ids es recursiva: se recorre como lista
            nombres.append(ids.ID().getText())
            ids = ids.ids()
        self.analizador.declarar_variables(nombres, ctx.tipo().getText(), ctx.start.line)

    # ------------------------------------------------------------------
    # Funciones
    # func: rtype ID LPAREN params RPAREN LBRACK vars body RBRACK SEMI
    # ------------------------------------------------------------------
    def enterFunc(self, ctx):
        self.analizador.inicio_funcion(ctx.ID().getText(), ctx.rtype().getText(), ctx.start.line)
        funcion = self.analizador.ambito
        funcion.inicio = self.generador.fila.siguiente()

        # params: plist | epsilon       plist: ID COLON tipo (COMMA plist)?
        plist = ctx.params().plist()
        while plist is not None:
            self.analizador.agregar_parametro(
                plist.ID().getText(), plist.tipo().getText(), plist.start.line)
            plist = plist.plist()

    def exitFunc(self, ctx):
        self.generador.terminar_funcion()                      # (ENDFUNC, -, -, -)
        self.analizador.fin_funcion(ctx.start.line)

    # call: ID LPAREN args RPAREN   (como estatuto  f(1);  o dentro de un factor)
    def enterCall(self, ctx):
        self.generador.abrir_llamada(ctx.ID().getText(), ctx.start.line)

    def exitCall(self, ctx):
        en_expresion = isinstance(ctx.parentCtx, LangParser.FactorContext)
        self.generador.cerrar_llamada(ctx.ID().getText(), ctx.start.line, en_expresion)

    # ------------------------------------------------------------------
    # Estatutos lineales (al salir, el valor de la expresion ya esta en la pila)
    # ------------------------------------------------------------------
    # assign: ID ASSIGN expresion SEMI
    def exitAssign(self, ctx):
        self.generador.asignar(ctx.ID().getText(), ctx.start.line)

    # readStmt: READ LPAREN ID RPAREN SEMI
    def exitReadStmt(self, ctx):
        self.generador.leer(ctx.ID().getText(), ctx.start.line)

    # returnStmt: RETURN expresion SEMI
    def exitReturnStmt(self, ctx):
        self.generador.regresar(ctx.start.line)

    # parg: expresion | CTE_STRING        print(a + 1, "hola")
    def exitParg(self, ctx):
        if ctx.CTE_STRING() is not None:
            self.generador.imprimir_letrero(ctx.CTE_STRING().getText())
        else:
            self.generador.imprimir_expresion()

    # ------------------------------------------------------------------
    # Estatutos de control
    # ------------------------------------------------------------------
    # condition: IF LPAREN expresion RPAREN body elsep SEMI
    def exitCondition(self, ctx):
        self.generador.cerrar_if()

    # elsep: ELSE body | epsilon
    def enterElsep(self, ctx):
        if ctx.ELSE() is not None:
            self.generador.iniciar_else()

    # cycle: WHILE LPAREN expresion RPAREN DO body SEMI
    def enterCycle(self, ctx):
        self.generador.iniciar_ciclo()

    def exitCycle(self, ctx):
        self.generador.cerrar_ciclo()

    # ------------------------------------------------------------------
    # Expresiones
    # ------------------------------------------------------------------
    # expresion: exp | exp rel exp
    def enterExpresion(self, ctx):
        if ctx.rel() is not None:
            self.generador.meter_operador(ctx.rel().getText())

    def exitExpresion(self, ctx):
        if ctx.rel() is not None:
            self.generador.reducir(ctx.start.line)

        # Si es la condicion de un if o de un while, ya se puede generar el GOTOF
        padre = ctx.parentCtx
        if isinstance(padre, (LangParser.ConditionContext, LangParser.CycleContext)):
            self.generador.generar_gotof(ctx.start.line)

    # exp: termino | exp PLUS termino | exp MINUS termino
    def enterExp(self, ctx):
        if ctx.PLUS() is not None:
            self.generador.meter_operador("+")
        elif ctx.MINUS() is not None:
            self.generador.meter_operador("-")

    def exitExp(self, ctx):
        if ctx.PLUS() is not None or ctx.MINUS() is not None:
            self.generador.reducir(ctx.start.line)

    # termino: factor | termino MULT factor | termino DIV factor
    def enterTermino(self, ctx):
        if ctx.MULT() is not None:
            self.generador.meter_operador("*")
        elif ctx.DIV() is not None:
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
            return                    # el resultado de la expresion ya esta en la pila

        if ctx.call() is not None:
            return                    # exitCall ya apilo el resultado de la llamada

        if ctx.ID() is not None:
            self.generador.operando_variable(ctx.ID().getText(), linea)
        elif ctx.cte().CTE_INT() is not None:
            self.generador.operando_constante(ctx.cte().getText(), "int")
        else:
            self.generador.operando_constante(ctx.cte().getText(), "float")

        # Signo unario: '+x' no cambia nada, '-x' se traduce como 0 - x
        if ctx.sign() is not None and ctx.sign().MINUS() is not None:
            self.generador.negar(linea)
