# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#programa.
    def enterPrograma(self, ctx:LangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LangParser#programa.
    def exitPrograma(self, ctx:LangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LangParser#vars.
    def enterVars(self, ctx:LangParser.VarsContext):
        pass

    # Exit a parse tree produced by LangParser#vars.
    def exitVars(self, ctx:LangParser.VarsContext):
        pass


    # Enter a parse tree produced by LangParser#decls.
    def enterDecls(self, ctx:LangParser.DeclsContext):
        pass

    # Exit a parse tree produced by LangParser#decls.
    def exitDecls(self, ctx:LangParser.DeclsContext):
        pass


    # Enter a parse tree produced by LangParser#decl.
    def enterDecl(self, ctx:LangParser.DeclContext):
        pass

    # Exit a parse tree produced by LangParser#decl.
    def exitDecl(self, ctx:LangParser.DeclContext):
        pass


    # Enter a parse tree produced by LangParser#ids.
    def enterIds(self, ctx:LangParser.IdsContext):
        pass

    # Exit a parse tree produced by LangParser#ids.
    def exitIds(self, ctx:LangParser.IdsContext):
        pass


    # Enter a parse tree produced by LangParser#tipo.
    def enterTipo(self, ctx:LangParser.TipoContext):
        pass

    # Exit a parse tree produced by LangParser#tipo.
    def exitTipo(self, ctx:LangParser.TipoContext):
        pass


    # Enter a parse tree produced by LangParser#funcs.
    def enterFuncs(self, ctx:LangParser.FuncsContext):
        pass

    # Exit a parse tree produced by LangParser#funcs.
    def exitFuncs(self, ctx:LangParser.FuncsContext):
        pass


    # Enter a parse tree produced by LangParser#func.
    def enterFunc(self, ctx:LangParser.FuncContext):
        pass

    # Exit a parse tree produced by LangParser#func.
    def exitFunc(self, ctx:LangParser.FuncContext):
        pass


    # Enter a parse tree produced by LangParser#rtype.
    def enterRtype(self, ctx:LangParser.RtypeContext):
        pass

    # Exit a parse tree produced by LangParser#rtype.
    def exitRtype(self, ctx:LangParser.RtypeContext):
        pass


    # Enter a parse tree produced by LangParser#params.
    def enterParams(self, ctx:LangParser.ParamsContext):
        pass

    # Exit a parse tree produced by LangParser#params.
    def exitParams(self, ctx:LangParser.ParamsContext):
        pass


    # Enter a parse tree produced by LangParser#plist.
    def enterPlist(self, ctx:LangParser.PlistContext):
        pass

    # Exit a parse tree produced by LangParser#plist.
    def exitPlist(self, ctx:LangParser.PlistContext):
        pass


    # Enter a parse tree produced by LangParser#body.
    def enterBody(self, ctx:LangParser.BodyContext):
        pass

    # Exit a parse tree produced by LangParser#body.
    def exitBody(self, ctx:LangParser.BodyContext):
        pass


    # Enter a parse tree produced by LangParser#stmts.
    def enterStmts(self, ctx:LangParser.StmtsContext):
        pass

    # Exit a parse tree produced by LangParser#stmts.
    def exitStmts(self, ctx:LangParser.StmtsContext):
        pass


    # Enter a parse tree produced by LangParser#statement.
    def enterStatement(self, ctx:LangParser.StatementContext):
        pass

    # Exit a parse tree produced by LangParser#statement.
    def exitStatement(self, ctx:LangParser.StatementContext):
        pass


    # Enter a parse tree produced by LangParser#assign.
    def enterAssign(self, ctx:LangParser.AssignContext):
        pass

    # Exit a parse tree produced by LangParser#assign.
    def exitAssign(self, ctx:LangParser.AssignContext):
        pass


    # Enter a parse tree produced by LangParser#printStmt.
    def enterPrintStmt(self, ctx:LangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by LangParser#printStmt.
    def exitPrintStmt(self, ctx:LangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by LangParser#pargs.
    def enterPargs(self, ctx:LangParser.PargsContext):
        pass

    # Exit a parse tree produced by LangParser#pargs.
    def exitPargs(self, ctx:LangParser.PargsContext):
        pass


    # Enter a parse tree produced by LangParser#parg.
    def enterParg(self, ctx:LangParser.PargContext):
        pass

    # Exit a parse tree produced by LangParser#parg.
    def exitParg(self, ctx:LangParser.PargContext):
        pass


    # Enter a parse tree produced by LangParser#readStmt.
    def enterReadStmt(self, ctx:LangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by LangParser#readStmt.
    def exitReadStmt(self, ctx:LangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by LangParser#returnStmt.
    def enterReturnStmt(self, ctx:LangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by LangParser#returnStmt.
    def exitReturnStmt(self, ctx:LangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by LangParser#cycle.
    def enterCycle(self, ctx:LangParser.CycleContext):
        pass

    # Exit a parse tree produced by LangParser#cycle.
    def exitCycle(self, ctx:LangParser.CycleContext):
        pass


    # Enter a parse tree produced by LangParser#condition.
    def enterCondition(self, ctx:LangParser.ConditionContext):
        pass

    # Exit a parse tree produced by LangParser#condition.
    def exitCondition(self, ctx:LangParser.ConditionContext):
        pass


    # Enter a parse tree produced by LangParser#elsep.
    def enterElsep(self, ctx:LangParser.ElsepContext):
        pass

    # Exit a parse tree produced by LangParser#elsep.
    def exitElsep(self, ctx:LangParser.ElsepContext):
        pass


    # Enter a parse tree produced by LangParser#fCall.
    def enterFCall(self, ctx:LangParser.FCallContext):
        pass

    # Exit a parse tree produced by LangParser#fCall.
    def exitFCall(self, ctx:LangParser.FCallContext):
        pass


    # Enter a parse tree produced by LangParser#call.
    def enterCall(self, ctx:LangParser.CallContext):
        pass

    # Exit a parse tree produced by LangParser#call.
    def exitCall(self, ctx:LangParser.CallContext):
        pass


    # Enter a parse tree produced by LangParser#args.
    def enterArgs(self, ctx:LangParser.ArgsContext):
        pass

    # Exit a parse tree produced by LangParser#args.
    def exitArgs(self, ctx:LangParser.ArgsContext):
        pass


    # Enter a parse tree produced by LangParser#alist.
    def enterAlist(self, ctx:LangParser.AlistContext):
        pass

    # Exit a parse tree produced by LangParser#alist.
    def exitAlist(self, ctx:LangParser.AlistContext):
        pass


    # Enter a parse tree produced by LangParser#expresion.
    def enterExpresion(self, ctx:LangParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LangParser#expresion.
    def exitExpresion(self, ctx:LangParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LangParser#rel.
    def enterRel(self, ctx:LangParser.RelContext):
        pass

    # Exit a parse tree produced by LangParser#rel.
    def exitRel(self, ctx:LangParser.RelContext):
        pass


    # Enter a parse tree produced by LangParser#exp.
    def enterExp(self, ctx:LangParser.ExpContext):
        pass

    # Exit a parse tree produced by LangParser#exp.
    def exitExp(self, ctx:LangParser.ExpContext):
        pass


    # Enter a parse tree produced by LangParser#termino.
    def enterTermino(self, ctx:LangParser.TerminoContext):
        pass

    # Exit a parse tree produced by LangParser#termino.
    def exitTermino(self, ctx:LangParser.TerminoContext):
        pass


    # Enter a parse tree produced by LangParser#factor.
    def enterFactor(self, ctx:LangParser.FactorContext):
        pass

    # Exit a parse tree produced by LangParser#factor.
    def exitFactor(self, ctx:LangParser.FactorContext):
        pass


    # Enter a parse tree produced by LangParser#sign.
    def enterSign(self, ctx:LangParser.SignContext):
        pass

    # Exit a parse tree produced by LangParser#sign.
    def exitSign(self, ctx:LangParser.SignContext):
        pass


    # Enter a parse tree produced by LangParser#cte.
    def enterCte(self, ctx:LangParser.CteContext):
        pass

    # Exit a parse tree produced by LangParser#cte.
    def exitCte(self, ctx:LangParser.CteContext):
        pass



del LangParser