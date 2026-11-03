# Generated from Lang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,286,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,82,
        8,1,1,2,1,2,1,2,1,2,3,2,88,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,3,4,99,8,4,1,5,1,5,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,3,8,122,8,8,1,9,1,9,3,9,126,
        8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,137,8,10,1,
        11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,147,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,3,13,156,8,13,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,174,8,
        16,1,17,1,17,3,17,178,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,3,22,209,8,22,1,23,1,
        23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,3,25,221,8,25,1,26,1,
        26,1,26,1,26,1,26,3,26,228,8,26,1,27,1,27,1,27,1,27,1,27,3,27,235,
        8,27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,5,29,
        248,8,29,10,29,12,29,251,9,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,5,30,262,8,30,10,30,12,30,265,9,30,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,280,8,31,1,32,
        1,32,1,33,1,33,1,33,0,2,58,60,34,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        0,4,1,0,5,6,1,0,20,22,1,0,16,17,1,0,32,33,280,0,68,1,0,0,0,2,81,
        1,0,0,0,4,87,1,0,0,0,6,89,1,0,0,0,8,98,1,0,0,0,10,100,1,0,0,0,12,
        106,1,0,0,0,14,108,1,0,0,0,16,121,1,0,0,0,18,125,1,0,0,0,20,136,
        1,0,0,0,22,138,1,0,0,0,24,146,1,0,0,0,26,155,1,0,0,0,28,157,1,0,
        0,0,30,162,1,0,0,0,32,173,1,0,0,0,34,177,1,0,0,0,36,179,1,0,0,0,
        38,185,1,0,0,0,40,189,1,0,0,0,42,197,1,0,0,0,44,208,1,0,0,0,46,210,
        1,0,0,0,48,213,1,0,0,0,50,220,1,0,0,0,52,227,1,0,0,0,54,234,1,0,
        0,0,56,236,1,0,0,0,58,238,1,0,0,0,60,252,1,0,0,0,62,279,1,0,0,0,
        64,281,1,0,0,0,66,283,1,0,0,0,68,69,5,1,0,0,69,70,5,35,0,0,70,71,
        5,23,0,0,71,72,3,2,1,0,72,73,3,12,6,0,73,74,5,2,0,0,74,75,3,22,11,
        0,75,76,5,3,0,0,76,77,5,0,0,1,77,1,1,0,0,0,78,79,5,4,0,0,79,82,3,
        4,2,0,80,82,1,0,0,0,81,78,1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,
        88,3,6,3,0,84,85,3,6,3,0,85,86,3,4,2,0,86,88,1,0,0,0,87,83,1,0,0,
        0,87,84,1,0,0,0,88,5,1,0,0,0,89,90,3,8,4,0,90,91,5,24,0,0,91,92,
        3,10,5,0,92,93,5,23,0,0,93,7,1,0,0,0,94,99,5,35,0,0,95,96,5,35,0,
        0,96,97,5,25,0,0,97,99,3,8,4,0,98,94,1,0,0,0,98,95,1,0,0,0,99,9,
        1,0,0,0,100,101,7,0,0,0,101,11,1,0,0,0,102,103,3,14,7,0,103,104,
        3,12,6,0,104,107,1,0,0,0,105,107,1,0,0,0,106,102,1,0,0,0,106,105,
        1,0,0,0,107,13,1,0,0,0,108,109,3,16,8,0,109,110,5,35,0,0,110,111,
        5,26,0,0,111,112,3,18,9,0,112,113,5,27,0,0,113,114,5,30,0,0,114,
        115,3,2,1,0,115,116,3,22,11,0,116,117,5,31,0,0,117,118,5,23,0,0,
        118,15,1,0,0,0,119,122,5,7,0,0,120,122,3,10,5,0,121,119,1,0,0,0,
        121,120,1,0,0,0,122,17,1,0,0,0,123,126,3,20,10,0,124,126,1,0,0,0,
        125,123,1,0,0,0,125,124,1,0,0,0,126,19,1,0,0,0,127,128,5,35,0,0,
        128,129,5,24,0,0,129,137,3,10,5,0,130,131,5,35,0,0,131,132,5,24,
        0,0,132,133,3,10,5,0,133,134,5,25,0,0,134,135,3,20,10,0,135,137,
        1,0,0,0,136,127,1,0,0,0,136,130,1,0,0,0,137,21,1,0,0,0,138,139,5,
        28,0,0,139,140,3,24,12,0,140,141,5,29,0,0,141,23,1,0,0,0,142,143,
        3,26,13,0,143,144,3,24,12,0,144,147,1,0,0,0,145,147,1,0,0,0,146,
        142,1,0,0,0,146,145,1,0,0,0,147,25,1,0,0,0,148,156,3,28,14,0,149,
        156,3,42,21,0,150,156,3,40,20,0,151,156,3,46,23,0,152,156,3,30,15,
        0,153,156,3,36,18,0,154,156,3,38,19,0,155,148,1,0,0,0,155,149,1,
        0,0,0,155,150,1,0,0,0,155,151,1,0,0,0,155,152,1,0,0,0,155,153,1,
        0,0,0,155,154,1,0,0,0,156,27,1,0,0,0,157,158,5,35,0,0,158,159,5,
        15,0,0,159,160,3,54,27,0,160,161,5,23,0,0,161,29,1,0,0,0,162,163,
        5,8,0,0,163,164,5,26,0,0,164,165,3,32,16,0,165,166,5,27,0,0,166,
        167,5,23,0,0,167,31,1,0,0,0,168,174,3,34,17,0,169,170,3,34,17,0,
        170,171,5,25,0,0,171,172,3,32,16,0,172,174,1,0,0,0,173,168,1,0,0,
        0,173,169,1,0,0,0,174,33,1,0,0,0,175,178,3,54,27,0,176,178,5,34,
        0,0,177,175,1,0,0,0,177,176,1,0,0,0,178,35,1,0,0,0,179,180,5,13,
        0,0,180,181,5,26,0,0,181,182,5,35,0,0,182,183,5,27,0,0,183,184,5,
        23,0,0,184,37,1,0,0,0,185,186,5,14,0,0,186,187,3,54,27,0,187,188,
        5,23,0,0,188,39,1,0,0,0,189,190,5,11,0,0,190,191,5,26,0,0,191,192,
        3,54,27,0,192,193,5,27,0,0,193,194,5,12,0,0,194,195,3,22,11,0,195,
        196,5,23,0,0,196,41,1,0,0,0,197,198,5,9,0,0,198,199,5,26,0,0,199,
        200,3,54,27,0,200,201,5,27,0,0,201,202,3,22,11,0,202,203,3,44,22,
        0,203,204,5,23,0,0,204,43,1,0,0,0,205,206,5,10,0,0,206,209,3,22,
        11,0,207,209,1,0,0,0,208,205,1,0,0,0,208,207,1,0,0,0,209,45,1,0,
        0,0,210,211,3,48,24,0,211,212,5,23,0,0,212,47,1,0,0,0,213,214,5,
        35,0,0,214,215,5,26,0,0,215,216,3,50,25,0,216,217,5,27,0,0,217,49,
        1,0,0,0,218,221,3,52,26,0,219,221,1,0,0,0,220,218,1,0,0,0,220,219,
        1,0,0,0,221,51,1,0,0,0,222,228,3,54,27,0,223,224,3,54,27,0,224,225,
        5,25,0,0,225,226,3,52,26,0,226,228,1,0,0,0,227,222,1,0,0,0,227,223,
        1,0,0,0,228,53,1,0,0,0,229,235,3,58,29,0,230,231,3,58,29,0,231,232,
        3,56,28,0,232,233,3,58,29,0,233,235,1,0,0,0,234,229,1,0,0,0,234,
        230,1,0,0,0,235,55,1,0,0,0,236,237,7,1,0,0,237,57,1,0,0,0,238,239,
        6,29,-1,0,239,240,3,60,30,0,240,249,1,0,0,0,241,242,10,2,0,0,242,
        243,5,16,0,0,243,248,3,60,30,0,244,245,10,1,0,0,245,246,5,17,0,0,
        246,248,3,60,30,0,247,241,1,0,0,0,247,244,1,0,0,0,248,251,1,0,0,
        0,249,247,1,0,0,0,249,250,1,0,0,0,250,59,1,0,0,0,251,249,1,0,0,0,
        252,253,6,30,-1,0,253,254,3,62,31,0,254,263,1,0,0,0,255,256,10,2,
        0,0,256,257,5,18,0,0,257,262,3,62,31,0,258,259,10,1,0,0,259,260,
        5,19,0,0,260,262,3,62,31,0,261,255,1,0,0,0,261,258,1,0,0,0,262,265,
        1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,61,1,0,0,0,265,263,1,
        0,0,0,266,267,5,26,0,0,267,268,3,54,27,0,268,269,5,27,0,0,269,280,
        1,0,0,0,270,280,3,48,24,0,271,280,5,35,0,0,272,280,3,66,33,0,273,
        274,3,64,32,0,274,275,5,35,0,0,275,280,1,0,0,0,276,277,3,64,32,0,
        277,278,3,66,33,0,278,280,1,0,0,0,279,266,1,0,0,0,279,270,1,0,0,
        0,279,271,1,0,0,0,279,272,1,0,0,0,279,273,1,0,0,0,279,276,1,0,0,
        0,280,63,1,0,0,0,281,282,7,2,0,0,282,65,1,0,0,0,283,284,7,3,0,0,
        284,67,1,0,0,0,20,81,87,98,106,121,125,136,146,155,173,177,208,220,
        227,234,247,249,261,263,279
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'main'", "'end'", "'var'", 
                     "'int'", "'float'", "'void'", "'print'", "'if'", "'else'", 
                     "'while'", "'do'", "'read'", "'return'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'>'", "'<'", "'!='", "';'", "':'", 
                     "','", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "MAIN", "END", "VAR", "INT", 
                      "FLOAT", "VOID", "PRINT", "IF", "ELSE", "WHILE", "DO", 
                      "READ", "RETURN", "ASSIGN", "PLUS", "MINUS", "MULT", 
                      "DIV", "GT", "LT", "NEQ", "SEMI", "COLON", "COMMA", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "CTE_FLOAT", "CTE_INT", "CTE_STRING", "ID", 
                      "WS" ]

    RULE_programa = 0
    RULE_vars = 1
    RULE_decls = 2
    RULE_decl = 3
    RULE_ids = 4
    RULE_tipo = 5
    RULE_funcs = 6
    RULE_func = 7
    RULE_rtype = 8
    RULE_params = 9
    RULE_plist = 10
    RULE_body = 11
    RULE_stmts = 12
    RULE_statement = 13
    RULE_assign = 14
    RULE_printStmt = 15
    RULE_pargs = 16
    RULE_parg = 17
    RULE_readStmt = 18
    RULE_returnStmt = 19
    RULE_cycle = 20
    RULE_condition = 21
    RULE_elsep = 22
    RULE_fCall = 23
    RULE_call = 24
    RULE_args = 25
    RULE_alist = 26
    RULE_expresion = 27
    RULE_rel = 28
    RULE_exp = 29
    RULE_termino = 30
    RULE_factor = 31
    RULE_sign = 32
    RULE_cte = 33

    ruleNames =  [ "programa", "vars", "decls", "decl", "ids", "tipo", "funcs", 
                   "func", "rtype", "params", "plist", "body", "stmts", 
                   "statement", "assign", "printStmt", "pargs", "parg", 
                   "readStmt", "returnStmt", "cycle", "condition", "elsep", 
                   "fCall", "call", "args", "alist", "expresion", "rel", 
                   "exp", "termino", "factor", "sign", "cte" ]

    EOF = Token.EOF
    PROGRAM=1
    MAIN=2
    END=3
    VAR=4
    INT=5
    FLOAT=6
    VOID=7
    PRINT=8
    IF=9
    ELSE=10
    WHILE=11
    DO=12
    READ=13
    RETURN=14
    ASSIGN=15
    PLUS=16
    MINUS=17
    MULT=18
    DIV=19
    GT=20
    LT=21
    NEQ=22
    SEMI=23
    COLON=24
    COMMA=25
    LPAREN=26
    RPAREN=27
    LBRACE=28
    RBRACE=29
    LBRACK=30
    RBRACK=31
    CTE_FLOAT=32
    CTE_INT=33
    CTE_STRING=34
    ID=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(LangParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def vars_(self):
            return self.getTypedRuleContext(LangParser.VarsContext,0)


        def funcs(self):
            return self.getTypedRuleContext(LangParser.FuncsContext,0)


        def MAIN(self):
            return self.getToken(LangParser.MAIN, 0)

        def body(self):
            return self.getTypedRuleContext(LangParser.BodyContext,0)


        def END(self):
            return self.getToken(LangParser.END, 0)

        def EOF(self):
            return self.getToken(LangParser.EOF, 0)

        def getRuleIndex(self):
            return LangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LangParser.PROGRAM)
            self.state = 69
            self.match(LangParser.ID)
            self.state = 70
            self.match(LangParser.SEMI)
            self.state = 71
            self.vars_()
            self.state = 72
            self.funcs()
            self.state = 73
            self.match(LangParser.MAIN)
            self.state = 74
            self.body()
            self.state = 75
            self.match(LangParser.END)
            self.state = 76
            self.match(LangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LangParser.VAR, 0)

        def decls(self):
            return self.getTypedRuleContext(LangParser.DeclsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = LangParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(LangParser.VAR)
                self.state = 79
                self.decls()
                pass
            elif token in [2, 5, 6, 7, 28]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(LangParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(LangParser.DeclsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = LangParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.decl()
                self.state = 85
                self.decls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(LangParser.IdsContext,0)


        def COLON(self):
            return self.getToken(LangParser.COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangParser.TipoContext,0)


        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = LangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.ids()
            self.state = 90
            self.match(LangParser.COLON)
            self.state = 91
            self.tipo()
            self.state = 92
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def COMMA(self):
            return self.getToken(LangParser.COMMA, 0)

        def ids(self):
            return self.getTypedRuleContext(LangParser.IdsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_ids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds" ):
                listener.enterIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds" ):
                listener.exitIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = LangParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(LangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(LangParser.ID)
                self.state = 96
                self.match(LangParser.COMMA)
                self.state = 97
                self.ids()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(LangParser.FLOAT, 0)

        def getRuleIndex(self):
            return LangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = LangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(LangParser.FuncContext,0)


        def funcs(self):
            return self.getTypedRuleContext(LangParser.FuncsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs" ):
                return visitor.visitFuncs(self)
            else:
                return visitor.visitChildren(self)




    def funcs(self):

        localctx = LangParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcs)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.func()
                self.state = 103
                self.funcs()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rtype(self):
            return self.getTypedRuleContext(LangParser.RtypeContext,0)


        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(LangParser.ParamsContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def LBRACK(self):
            return self.getToken(LangParser.LBRACK, 0)

        def vars_(self):
            return self.getTypedRuleContext(LangParser.VarsContext,0)


        def body(self):
            return self.getTypedRuleContext(LangParser.BodyContext,0)


        def RBRACK(self):
            return self.getToken(LangParser.RBRACK, 0)

        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = LangParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.rtype()
            self.state = 109
            self.match(LangParser.ID)
            self.state = 110
            self.match(LangParser.LPAREN)
            self.state = 111
            self.params()
            self.state = 112
            self.match(LangParser.RPAREN)
            self.state = 113
            self.match(LangParser.LBRACK)
            self.state = 114
            self.vars_()
            self.state = 115
            self.body()
            self.state = 116
            self.match(LangParser.RBRACK)
            self.state = 117
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(LangParser.VOID, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangParser.TipoContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_rtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRtype" ):
                listener.enterRtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRtype" ):
                listener.exitRtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRtype" ):
                return visitor.visitRtype(self)
            else:
                return visitor.visitChildren(self)




    def rtype(self):

        localctx = LangParser.RtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rtype)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(LangParser.VOID)
                pass
            elif token in [5, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.tipo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plist(self):
            return self.getTypedRuleContext(LangParser.PlistContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = LangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.plist()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def COLON(self):
            return self.getToken(LangParser.COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangParser.TipoContext,0)


        def COMMA(self):
            return self.getToken(LangParser.COMMA, 0)

        def plist(self):
            return self.getTypedRuleContext(LangParser.PlistContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_plist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlist" ):
                listener.enterPlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlist" ):
                listener.exitPlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlist" ):
                return visitor.visitPlist(self)
            else:
                return visitor.visitChildren(self)




    def plist(self):

        localctx = LangParser.PlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_plist)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(LangParser.ID)
                self.state = 128
                self.match(LangParser.COLON)
                self.state = 129
                self.tipo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(LangParser.ID)
                self.state = 131
                self.match(LangParser.COLON)
                self.state = 132
                self.tipo()
                self.state = 133
                self.match(LangParser.COMMA)
                self.state = 134
                self.plist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(LangParser.LBRACE, 0)

        def stmts(self):
            return self.getTypedRuleContext(LangParser.StmtsContext,0)


        def RBRACE(self):
            return self.getToken(LangParser.RBRACE, 0)

        def getRuleIndex(self):
            return LangParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = LangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(LangParser.LBRACE)
            self.state = 139
            self.stmts()
            self.state = 140
            self.match(LangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(LangParser.StatementContext,0)


        def stmts(self):
            return self.getTypedRuleContext(LangParser.StmtsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = LangParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmts)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 11, 13, 14, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.statement()
                self.state = 143
                self.stmts()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(LangParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(LangParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(LangParser.CycleContext,0)


        def fCall(self):
            return self.getTypedRuleContext(LangParser.FCallContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(LangParser.PrintStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(LangParser.ReadStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(LangParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.fCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.printStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 153
                self.readStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 154
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(LangParser.ASSIGN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = LangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(LangParser.ID)
            self.state = 158
            self.match(LangParser.ASSIGN)
            self.state = 159
            self.expresion()
            self.state = 160
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(LangParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def pargs(self):
            return self.getTypedRuleContext(LangParser.PargsContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = LangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(LangParser.PRINT)
            self.state = 163
            self.match(LangParser.LPAREN)
            self.state = 164
            self.pargs()
            self.state = 165
            self.match(LangParser.RPAREN)
            self.state = 166
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PargsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parg(self):
            return self.getTypedRuleContext(LangParser.PargContext,0)


        def COMMA(self):
            return self.getToken(LangParser.COMMA, 0)

        def pargs(self):
            return self.getTypedRuleContext(LangParser.PargsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_pargs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPargs" ):
                listener.enterPargs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPargs" ):
                listener.exitPargs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPargs" ):
                return visitor.visitPargs(self)
            else:
                return visitor.visitChildren(self)




    def pargs(self):

        localctx = LangParser.PargsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pargs)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.parg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.parg()
                self.state = 170
                self.match(LangParser.COMMA)
                self.state = 171
                self.pargs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PargContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def CTE_STRING(self):
            return self.getToken(LangParser.CTE_STRING, 0)

        def getRuleIndex(self):
            return LangParser.RULE_parg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParg" ):
                listener.enterParg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParg" ):
                listener.exitParg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParg" ):
                return visitor.visitParg(self)
            else:
                return visitor.visitChildren(self)




    def parg(self):

        localctx = LangParser.PargContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parg)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 26, 32, 33, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.expresion()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(LangParser.CTE_STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(LangParser.READ, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)




    def readStmt(self):

        localctx = LangParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(LangParser.READ)
            self.state = 180
            self.match(LangParser.LPAREN)
            self.state = 181
            self.match(LangParser.ID)
            self.state = 182
            self.match(LangParser.RPAREN)
            self.state = 183
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LangParser.RETURN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = LangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(LangParser.RETURN)
            self.state = 186
            self.expresion()
            self.state = 187
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def DO(self):
            return self.getToken(LangParser.DO, 0)

        def body(self):
            return self.getTypedRuleContext(LangParser.BodyContext,0)


        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCycle" ):
                return visitor.visitCycle(self)
            else:
                return visitor.visitChildren(self)




    def cycle(self):

        localctx = LangParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(LangParser.WHILE)
            self.state = 190
            self.match(LangParser.LPAREN)
            self.state = 191
            self.expresion()
            self.state = 192
            self.match(LangParser.RPAREN)
            self.state = 193
            self.match(LangParser.DO)
            self.state = 194
            self.body()
            self.state = 195
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def body(self):
            return self.getTypedRuleContext(LangParser.BodyContext,0)


        def elsep(self):
            return self.getTypedRuleContext(LangParser.ElsepContext,0)


        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = LangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(LangParser.IF)
            self.state = 198
            self.match(LangParser.LPAREN)
            self.state = 199
            self.expresion()
            self.state = 200
            self.match(LangParser.RPAREN)
            self.state = 201
            self.body()
            self.state = 202
            self.elsep()
            self.state = 203
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LangParser.ELSE, 0)

        def body(self):
            return self.getTypedRuleContext(LangParser.BodyContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_elsep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsep" ):
                listener.enterElsep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsep" ):
                listener.exitElsep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsep" ):
                return visitor.visitElsep(self)
            else:
                return visitor.visitChildren(self)




    def elsep(self):

        localctx = LangParser.ElsepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elsep)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(LangParser.ELSE)
                self.state = 206
                self.body()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(LangParser.CallContext,0)


        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def getRuleIndex(self):
            return LangParser.RULE_fCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFCall" ):
                listener.enterFCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFCall" ):
                listener.exitFCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFCall" ):
                return visitor.visitFCall(self)
            else:
                return visitor.visitChildren(self)




    def fCall(self):

        localctx = LangParser.FCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.call()
            self.state = 211
            self.match(LangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(LangParser.ArgsContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def getRuleIndex(self):
            return LangParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = LangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(LangParser.ID)
            self.state = 214
            self.match(LangParser.LPAREN)
            self.state = 215
            self.args()
            self.state = 216
            self.match(LangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alist(self):
            return self.getTypedRuleContext(LangParser.AlistContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = LangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_args)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 26, 32, 33, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.alist()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def COMMA(self):
            return self.getToken(LangParser.COMMA, 0)

        def alist(self):
            return self.getTypedRuleContext(LangParser.AlistContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_alist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlist" ):
                listener.enterAlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlist" ):
                listener.exitAlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlist" ):
                return visitor.visitAlist(self)
            else:
                return visitor.visitChildren(self)




    def alist(self):

        localctx = LangParser.AlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_alist)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.expresion()
                self.state = 224
                self.match(LangParser.COMMA)
                self.state = 225
                self.alist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExpContext)
            else:
                return self.getTypedRuleContext(LangParser.ExpContext,i)


        def rel(self):
            return self.getTypedRuleContext(LangParser.RelContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = LangParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expresion)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.exp(0)
                self.state = 231
                self.rel()
                self.state = 232
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(LangParser.GT, 0)

        def LT(self):
            return self.getToken(LangParser.LT, 0)

        def NEQ(self):
            return self.getToken(LangParser.NEQ, 0)

        def getRuleIndex(self):
            return LangParser.RULE_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel" ):
                listener.enterRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel" ):
                listener.exitRel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel" ):
                return visitor.visitRel(self)
            else:
                return visitor.visitChildren(self)




    def rel(self):

        localctx = LangParser.RelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(LangParser.TerminoContext,0)


        def exp(self):
            return self.getTypedRuleContext(LangParser.ExpContext,0)


        def PLUS(self):
            return self.getToken(LangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LangParser.MINUS, 0)

        def getRuleIndex(self):
            return LangParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 247
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 241
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 242
                        self.match(LangParser.PLUS)
                        self.state = 243
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 244
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 245
                        self.match(LangParser.MINUS)
                        self.state = 246
                        self.termino(0)
                        pass

             
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(LangParser.FactorContext,0)


        def termino(self):
            return self.getTypedRuleContext(LangParser.TerminoContext,0)


        def MULT(self):
            return self.getToken(LangParser.MULT, 0)

        def DIV(self):
            return self.getToken(LangParser.DIV, 0)

        def getRuleIndex(self):
            return LangParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 261
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 255
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 256
                        self.match(LangParser.MULT)
                        self.state = 257
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = LangParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 258
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 259
                        self.match(LangParser.DIV)
                        self.state = 260
                        self.factor()
                        pass

             
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LangParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def call(self):
            return self.getTypedRuleContext(LangParser.CallContext,0)


        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(LangParser.CteContext,0)


        def sign(self):
            return self.getTypedRuleContext(LangParser.SignContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = LangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_factor)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(LangParser.LPAREN)
                self.state = 267
                self.expresion()
                self.state = 268
                self.match(LangParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(LangParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.cte()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
                self.sign()
                self.state = 274
                self.match(LangParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 276
                self.sign()
                self.state = 277
                self.cte()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(LangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LangParser.MINUS, 0)

        def getRuleIndex(self):
            return LangParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = LangParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_INT(self):
            return self.getToken(LangParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(LangParser.CTE_FLOAT, 0)

        def getRuleIndex(self):
            return LangParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCte" ):
                return visitor.visitCte(self)
            else:
                return visitor.visitChildren(self)




    def cte(self):

        localctx = LangParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.exp_sempred
        self._predicates[30] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




