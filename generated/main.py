"""
BabyDuck - Scanner + Parser generados con ANTLR4 (target Python3)

Antes de usarlo, genera el scanner y el parser (necesita Java):
    pip install antlr4-tools antlr4-python3-runtime
    antlr4 -Dlanguage=Python3 Lang.g4

Uso (desde la raiz del repo):
    python -m generated.main programa.txt                 valida el programa
    python -m generated.main programa.txt --tokens        ademas lista los tokens
    python -m generated.main programa.txt --tree          ademas imprime el arbol de derivacion
    python -m generated.main programa.txt --tables        ademas imprime el directorio de funciones
    python -m generated.main programa.txt --cuadruplos    ademas imprime la fila de cuadruplos
"""
import sys

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from .LangLexer import LangLexer
from .LangParser import LangParser


class Recolector(ErrorListener):
    """Guarda los errores en una lista en vez de solo imprimirlos."""

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"línea {line}:{column} {msg}")


def construir(src):
    """Prepara scanner y parser, con un recolector de errores para cada uno."""
    lex_l, syn_l = Recolector(), Recolector()
    lexer = LangLexer(InputStream(src))
    lexer.removeErrorListeners()
    lexer.addErrorListener(lex_l)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(syn_l)
    return parser, stream, lex_l, syn_l


def analizar_texto(src, con_arbol=False):
    parser, stream, lex_l, syn_l = construir(src)
    arbol = parser.programa()      
    stream.fill()
    tokens = [
        (LangLexer.symbolicNames[t.type], t.text)
        for t in stream.tokens if t.type != -1     
    ]
    r = {"tokens": tokens, "lex_errors": lex_l.errores, "syn_errors": syn_l.errores}
    if con_arbol:
        r["arbol"] = arbol.toStringTree(recog=parser)
    return r


def analizar_semantica(src):
    """
    Corre el analisis semantico y genera los cuadruplos.

    Solo analiza si el programa no tiene errores lexicos ni de sintaxis.
    Devuelve (errores, directorio de funciones, fila de cuadruplos).
    """
    from semantics.listener import ListenerSemantico

    parser, stream, lex_l, syn_l = construir(src)
    arbol = parser.programa()
    if lex_l.errores or syn_l.errores:
        return [], None, None
    listener = ListenerSemantico()
    ParseTreeWalker().walk(listener, arbol)
    return listener.analizador.errores, listener.analizador.directorio, listener.generador.fila


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    ruta = sys.argv[1]
    with open(ruta, encoding="utf-8") as f:
        r = analizar_texto(f.read(), con_arbol="--tree" in sys.argv)

    if "--tokens" in sys.argv:
        for tipo, texto in r["tokens"]:
            print(f"{tipo:<11} {texto}")

    errores = r["lex_errors"] + r["syn_errors"]
    if errores:
        print(f"[ERROR] {ruta}")
        for e in errores:
            print("  ", e)
        sys.exit(1)

    if "--tree" in sys.argv:
        print(r["arbol"])

    with open(ruta, encoding="utf-8") as f:
        sem_errores, directorio, fila = analizar_semantica(f.read())
    if sem_errores:
        print(f"[ERROR SEMÁNTICO] {ruta}")
        for e in sem_errores:
            print("  ", e)
        sys.exit(1)
    if "--tables" in sys.argv:
        print(directorio.mostrar())
    if "--cuadruplos" in sys.argv:
        print(fila.mostrar())
    print(f"[OK] {ruta}: programa válido")


if __name__ == "__main__":
    main()