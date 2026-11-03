// Generated from /Users/ximenatobias/Documents/Tec/Semestres/SEMESTRE 8/patito/Lang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LangParser}.
 */
public interface LangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(LangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(LangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#declarations}.
	 * @param ctx the parse tree
	 */
	void enterDeclarations(LangParser.DeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#declarations}.
	 * @param ctx the parse tree
	 */
	void exitDeclarations(LangParser.DeclarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(LangParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(LangParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#functions}.
	 * @param ctx the parse tree
	 */
	void enterFunctions(LangParser.FunctionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#functions}.
	 * @param ctx the parse tree
	 */
	void exitFunctions(LangParser.FunctionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(LangParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(LangParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(LangParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(LangParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#mainBlock}.
	 * @param ctx the parse tree
	 */
	void enterMainBlock(LangParser.MainBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#mainBlock}.
	 * @param ctx the parse tree
	 */
	void exitMainBlock(LangParser.MainBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(LangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(LangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(LangParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(LangParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(LangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(LangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(LangParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(LangParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(LangParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(LangParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(LangParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(LangParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(LangParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(LangParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#addition}.
	 * @param ctx the parse tree
	 */
	void enterAddition(LangParser.AdditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#addition}.
	 * @param ctx the parse tree
	 */
	void exitAddition(LangParser.AdditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#multiplication}.
	 * @param ctx the parse tree
	 */
	void enterMultiplication(LangParser.MultiplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#multiplication}.
	 * @param ctx the parse tree
	 */
	void exitMultiplication(LangParser.MultiplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(LangParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(LangParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link LangParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(LangParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LangParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(LangParser.TypeContext ctx);
}