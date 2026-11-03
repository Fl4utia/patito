"""
Puntos neuralgicos de BabyDuck.

AnalizadorSemantico: cada metodo es un punto neuralgico con sus validaciones.
ListenerSemantico: listener de ANTLR que conecta el arbol de Lang.g4 con el analizador.

ANTLR llama a enterX al entrar a la regla X y a exitX al salir de ella.
Requiere haber generado LangListener.py con:  antlr4 -Dlanguage=Python3 Lang.g4
"""
try:
    from LangListener import LangListener
except ImportError:          # permite probar el analizador sin haber generado el codigo de ANTLR
    LangListener = object

from directorio_funciones import DirectorioFunciones, Funcion


class AnalizadorSemantico:
    """
    Decisiones de diseno (se pueden cambiar aqui):
      - Una variable local o un parametro PUEDE llamarse igual que una global
        (la local oculta a la global). Solo se rechaza el nombre repetido dentro
        del MISMO ambito.
      - Los errores se acumulan en self.errores y el analisis continua.
    """

    def __init__(self):
        self.directorio = None
        self.ambito = None          # Funcion en la que se esta (programa o funcion)
        self.errores = []

    def _error(self, linea, mensaje):
        self.errores.append(f"línea {linea}: {mensaje}")

    # Punto neuralgico 1: al entrar al programa
    def inicio_programa(self, nombre):
        self.directorio = DirectorioFunciones(nombre)
        self.ambito = self.directorio.obtener_funcion(nombre)

    # Punto neuralgico 2: al terminar una declaracion "ids : tipo ;"
    def declarar_variables(self, nombres, tipo, linea):
        for nombre in nombres:
            if not self.ambito.variables.agregar(nombre, tipo):
                self._error(linea, f"variable '{nombre}' doblemente declarada")

    # Punto neuralgico 3: al entrar a una funcion (despues de leer tipo e id)
    def inicio_funcion(self, nombre, retorno, linea):
        funcion = self.directorio.agregar_funcion(nombre, retorno)
        if funcion is None:
            self._error(linea, f"función '{nombre}' doblemente declarada")
            # Se analiza su cuerpo en una funcion desechable para no ensuciar el directorio
            funcion = Funcion(nombre, retorno)
        self.ambito = funcion

    # Punto neuralgico 4: por cada parametro "id : tipo"
    def agregar_parametro(self, nombre, tipo, linea):
        if not self.directorio.agregar_parametro(self.ambito, nombre, tipo):
            self._error(linea, f"parámetro '{nombre}' repetido en la función '{self.ambito.nombre}'")

    # Punto neuralgico 5: al salir de una funcion
    def fin_funcion(self):
        self.ambito = self.directorio.obtener_funcion(self.directorio.nombre_programa)

    # Punto neuralgico 6: al usar una variable (asignacion, read, factor)
    def usar_variable(self, nombre, linea):
        info = self.directorio.buscar_variable(nombre, self.ambito)
        if info is None:
            self._error(linea, f"variable '{nombre}' no declarada")
            return None
        return info["tipo"]

    # Punto neuralgico 7: al llamar una funcion
    def llamar_funcion(self, nombre, linea):
        funcion = self.directorio.obtener_funcion(nombre)
        if funcion is None or nombre == self.directorio.nombre_programa:
            self._error(linea, f"función '{nombre}' no declarada")
            return None
        return funcion


class ListenerSemantico(LangListener):
    def __init__(self):
        super().__init__()
        self.analizador = AnalizadorSemantico()

    # programa: PROGRAM ID SEMI vars funcs MAIN body END EOF
    def enterPrograma(self, ctx):
        self.analizador.inicio_programa(ctx.ID().getText())

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
        # params: plist | epsilon ;  plist es recursiva: ID COLON tipo (COMMA plist)?
        plist = ctx.params().plist()
        while plist is not None:
            self.analizador.agregar_parametro(
                plist.ID().getText(), plist.tipo().getText(), plist.start.line
            )
            plist = plist.plist()

    def exitFunc(self, ctx):
        self.analizador.fin_funcion()

    # assign: ID ASSIGN expresion SEMI
    def enterAssign(self, ctx):
        self.analizador.usar_variable(ctx.ID().getText(), ctx.start.line)

    # readStmt: READ LPAREN ID RPAREN SEMI
    def enterReadStmt(self, ctx):
        self.analizador.usar_variable(ctx.ID().getText(), ctx.start.line)

    # factor: LPAREN expresion RPAREN | call | ID | cte | sign ID | sign cte
    def enterFactor(self, ctx):
        if ctx.ID() is not None:
            self.analizador.usar_variable(ctx.ID().getText(), ctx.start.line)

    # call: ID LPAREN args RPAREN     (se usa en fCall y dentro de factor)
    def enterCall(self, ctx):
        self.analizador.llamar_funcion(ctx.ID().getText(), ctx.start.line)
