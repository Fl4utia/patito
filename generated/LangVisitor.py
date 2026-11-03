# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#programa.
    def visitPrograma(self, ctx:LangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#vars.
    def visitVars(self, ctx:LangParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#decls.
    def visitDecls(self, ctx:LangParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#decl.
    def visitDecl(self, ctx:LangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ids.
    def visitIds(self, ctx:LangParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#tipo.
    def visitTipo(self, ctx:LangParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#funcs.
    def visitFuncs(self, ctx:LangParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#func.
    def visitFunc(self, ctx:LangParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#rtype.
    def visitRtype(self, ctx:LangParser.RtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#params.
    def visitParams(self, ctx:LangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#plist.
    def visitPlist(self, ctx:LangParser.PlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#body.
    def visitBody(self, ctx:LangParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#stmts.
    def visitStmts(self, ctx:LangParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#statement.
    def visitStatement(self, ctx:LangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#assign.
    def visitAssign(self, ctx:LangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#printStmt.
    def visitPrintStmt(self, ctx:LangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#pargs.
    def visitPargs(self, ctx:LangParser.PargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#parg.
    def visitParg(self, ctx:LangParser.PargContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#readStmt.
    def visitReadStmt(self, ctx:LangParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#returnStmt.
    def visitReturnStmt(self, ctx:LangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#cycle.
    def visitCycle(self, ctx:LangParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#condition.
    def visitCondition(self, ctx:LangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#elsep.
    def visitElsep(self, ctx:LangParser.ElsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#fCall.
    def visitFCall(self, ctx:LangParser.FCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#call.
    def visitCall(self, ctx:LangParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#args.
    def visitArgs(self, ctx:LangParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#alist.
    def visitAlist(self, ctx:LangParser.AlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expresion.
    def visitExpresion(self, ctx:LangParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#rel.
    def visitRel(self, ctx:LangParser.RelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#exp.
    def visitExp(self, ctx:LangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#termino.
    def visitTermino(self, ctx:LangParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#factor.
    def visitFactor(self, ctx:LangParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#sign.
    def visitSign(self, ctx:LangParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#cte.
    def visitCte(self, ctx:LangParser.CteContext):
        return self.visitChildren(ctx)



del LangParser