// Generated from /Users/ximenatobias/Documents/Tec/Semestres/SEMESTRE 8/patito/Lang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, MAIN=2, END=3, VAR=4, INT=5, FLOAT=6, VOID=7, PRINT=8, IF=9, 
		ELSE=10, WHILE=11, DO=12, READ=13, RETURN=14, ASSIGN=15, PLUS=16, MINUS=17, 
		MULT=18, DIV=19, GT=20, LT=21, NEQ=22, SEMI=23, COLON=24, COMMA=25, LPAREN=26, 
		RPAREN=27, LBRACE=28, RBRACE=29, LBRACK=30, RBRACK=31, CTE_FLOAT=32, CTE_INT=33, 
		CTE_STRING=34, ID=35, WS=36;
	public static final int
		RULE_programa = 0, RULE_vars = 1, RULE_decls = 2, RULE_decl = 3, RULE_ids = 4, 
		RULE_tipo = 5, RULE_funcs = 6, RULE_func = 7, RULE_rtype = 8, RULE_params = 9, 
		RULE_plist = 10, RULE_body = 11, RULE_stmts = 12, RULE_statement = 13, 
		RULE_assign = 14, RULE_printStmt = 15, RULE_pargs = 16, RULE_parg = 17, 
		RULE_readStmt = 18, RULE_returnStmt = 19, RULE_cycle = 20, RULE_condition = 21, 
		RULE_elsep = 22, RULE_fCall = 23, RULE_call = 24, RULE_args = 25, RULE_alist = 26, 
		RULE_expresion = 27, RULE_rel = 28, RULE_exp = 29, RULE_termino = 30, 
		RULE_factor = 31, RULE_sign = 32, RULE_cte = 33;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "vars", "decls", "decl", "ids", "tipo", "funcs", "func", 
			"rtype", "params", "plist", "body", "stmts", "statement", "assign", "printStmt", 
			"pargs", "parg", "readStmt", "returnStmt", "cycle", "condition", "elsep", 
			"fCall", "call", "args", "alist", "expresion", "rel", "exp", "termino", 
			"factor", "sign", "cte"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'main'", "'end'", "'var'", "'int'", "'float'", "'void'", 
			"'print'", "'if'", "'else'", "'while'", "'do'", "'read'", "'return'", 
			"'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'!='", "';'", "':'", 
			"','", "'('", "')'", "'{'", "'}'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "MAIN", "END", "VAR", "INT", "FLOAT", "VOID", "PRINT", 
			"IF", "ELSE", "WHILE", "DO", "READ", "RETURN", "ASSIGN", "PLUS", "MINUS", 
			"MULT", "DIV", "GT", "LT", "NEQ", "SEMI", "COLON", "COMMA", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "CTE_FLOAT", "CTE_INT", 
			"CTE_STRING", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Lang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(LangParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public TerminalNode MAIN() { return getToken(LangParser.MAIN, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode END() { return getToken(LangParser.END, 0); }
		public TerminalNode EOF() { return getToken(LangParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(PROGRAM);
			setState(69);
			match(ID);
			setState(70);
			match(SEMI);
			setState(71);
			vars();
			setState(72);
			funcs();
			setState(73);
			match(MAIN);
			setState(74);
			body();
			setState(75);
			match(END);
			setState(76);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(LangParser.VAR, 0); }
		public DeclsContext decls() {
			return getRuleContext(DeclsContext.class,0);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vars);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				match(VAR);
				setState(79);
				decls();
				}
				break;
			case MAIN:
			case INT:
			case FLOAT:
			case VOID:
			case LBRACE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclsContext extends ParserRuleContext {
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public DeclsContext decls() {
			return getRuleContext(DeclsContext.class,0);
		}
		public DeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decls; }
	}

	public final DeclsContext decls() throws RecognitionException {
		DeclsContext _localctx = new DeclsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_decls);
		try {
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				decl();
				setState(85);
				decls();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclContext extends ParserRuleContext {
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			ids();
			setState(90);
			match(COLON);
			setState(91);
			tipo();
			setState(92);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode COMMA() { return getToken(LangParser.COMMA, 0); }
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public IdsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ids; }
	}

	public final IdsContext ids() throws RecognitionException {
		IdsContext _localctx = new IdsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ids);
		try {
			setState(98);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				match(ID);
				setState(96);
				match(COMMA);
				setState(97);
				ids();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(LangParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(LangParser.FLOAT, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcs);
		try {
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case VOID:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				func();
				setState(103);
				funcs();
				}
				break;
			case MAIN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncContext extends ParserRuleContext {
		public RtypeContext rtype() {
			return getRuleContext(RtypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public TerminalNode LBRACK() { return getToken(LangParser.LBRACK, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode RBRACK() { return getToken(LangParser.RBRACK, 0); }
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			rtype();
			setState(109);
			match(ID);
			setState(110);
			match(LPAREN);
			setState(111);
			params();
			setState(112);
			match(RPAREN);
			setState(113);
			match(LBRACK);
			setState(114);
			vars();
			setState(115);
			body();
			setState(116);
			match(RBRACK);
			setState(117);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RtypeContext extends ParserRuleContext {
		public TerminalNode VOID() { return getToken(LangParser.VOID, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public RtypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rtype; }
	}

	public final RtypeContext rtype() throws RecognitionException {
		RtypeContext _localctx = new RtypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_rtype);
		try {
			setState(121);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VOID:
				enterOuterAlt(_localctx, 1);
				{
				setState(119);
				match(VOID);
				}
				break;
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(120);
				tipo();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public PlistContext plist() {
			return getRuleContext(PlistContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_params);
		try {
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				plist();
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PlistContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode COLON() { return getToken(LangParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(LangParser.COMMA, 0); }
		public PlistContext plist() {
			return getRuleContext(PlistContext.class,0);
		}
		public PlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_plist; }
	}

	public final PlistContext plist() throws RecognitionException {
		PlistContext _localctx = new PlistContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_plist);
		try {
			setState(136);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				match(ID);
				setState(128);
				match(COLON);
				setState(129);
				tipo();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				match(ID);
				setState(131);
				match(COLON);
				setState(132);
				tipo();
				setState(133);
				match(COMMA);
				setState(134);
				plist();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(LangParser.LBRACE, 0); }
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(LangParser.RBRACE, 0); }
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(LBRACE);
			setState(139);
			stmts();
			setState(140);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtsContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public StmtsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmts; }
	}

	public final StmtsContext stmts() throws RecognitionException {
		StmtsContext _localctx = new StmtsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_stmts);
		try {
			setState(146);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
			case IF:
			case WHILE:
			case READ:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				statement();
				setState(143);
				stmts();
				}
				break;
			case RBRACE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public FCallContext fCall() {
			return getRuleContext(FCallContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public ReadStmtContext readStmt() {
			return getRuleContext(ReadStmtContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_statement);
		try {
			setState(155);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(150);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(151);
				fCall();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(152);
				printStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(153);
				readStmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(154);
				returnStmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(LangParser.ASSIGN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(ID);
			setState(158);
			match(ASSIGN);
			setState(159);
			expresion();
			setState(160);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(LangParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public PargsContext pargs() {
			return getRuleContext(PargsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_printStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(PRINT);
			setState(163);
			match(LPAREN);
			setState(164);
			pargs();
			setState(165);
			match(RPAREN);
			setState(166);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PargsContext extends ParserRuleContext {
		public PargContext parg() {
			return getRuleContext(PargContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(LangParser.COMMA, 0); }
		public PargsContext pargs() {
			return getRuleContext(PargsContext.class,0);
		}
		public PargsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pargs; }
	}

	public final PargsContext pargs() throws RecognitionException {
		PargsContext _localctx = new PargsContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_pargs);
		try {
			setState(173);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(168);
				parg();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(169);
				parg();
				setState(170);
				match(COMMA);
				setState(171);
				pargs();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PargContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CTE_STRING() { return getToken(LangParser.CTE_STRING, 0); }
		public PargContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parg; }
	}

	public final PargContext parg() throws RecognitionException {
		PargContext _localctx = new PargContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_parg);
		try {
			setState(177);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case LPAREN:
			case CTE_FLOAT:
			case CTE_INT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(175);
				expresion();
				}
				break;
			case CTE_STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(176);
				match(CTE_STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadStmtContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(LangParser.READ, 0); }
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public ReadStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_readStmt; }
	}

	public final ReadStmtContext readStmt() throws RecognitionException {
		ReadStmtContext _localctx = new ReadStmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_readStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			match(READ);
			setState(180);
			match(LPAREN);
			setState(181);
			match(ID);
			setState(182);
			match(RPAREN);
			setState(183);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(LangParser.RETURN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_returnStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(RETURN);
			setState(186);
			expresion();
			setState(187);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(LangParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public TerminalNode DO() { return getToken(LangParser.DO, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			match(WHILE);
			setState(190);
			match(LPAREN);
			setState(191);
			expresion();
			setState(192);
			match(RPAREN);
			setState(193);
			match(DO);
			setState(194);
			body();
			setState(195);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(LangParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ElsepContext elsep() {
			return getRuleContext(ElsepContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(IF);
			setState(198);
			match(LPAREN);
			setState(199);
			expresion();
			setState(200);
			match(RPAREN);
			setState(201);
			body();
			setState(202);
			elsep();
			setState(203);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElsepContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(LangParser.ELSE, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ElsepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elsep; }
	}

	public final ElsepContext elsep() throws RecognitionException {
		ElsepContext _localctx = new ElsepContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_elsep);
		try {
			setState(208);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ELSE:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				match(ELSE);
				setState(206);
				body();
				}
				break;
			case SEMI:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FCallContext extends ParserRuleContext {
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(LangParser.SEMI, 0); }
		public FCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fCall; }
	}

	public final FCallContext fCall() throws RecognitionException {
		FCallContext _localctx = new FCallContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_fCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			call();
			setState(211);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(ID);
			setState(214);
			match(LPAREN);
			setState(215);
			args();
			setState(216);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public AlistContext alist() {
			return getRuleContext(AlistContext.class,0);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_args);
		try {
			setState(220);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case LPAREN:
			case CTE_FLOAT:
			case CTE_INT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(218);
				alist();
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AlistContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(LangParser.COMMA, 0); }
		public AlistContext alist() {
			return getRuleContext(AlistContext.class,0);
		}
		public AlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alist; }
	}

	public final AlistContext alist() throws RecognitionException {
		AlistContext _localctx = new AlistContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_alist);
		try {
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(223);
				expresion();
				setState(224);
				match(COMMA);
				setState(225);
				alist();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public RelContext rel() {
			return getRuleContext(RelContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expresion);
		try {
			setState(234);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(229);
				exp(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(230);
				exp(0);
				setState(231);
				rel();
				setState(232);
				exp(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelContext extends ParserRuleContext {
		public TerminalNode GT() { return getToken(LangParser.GT, 0); }
		public TerminalNode LT() { return getToken(LangParser.LT, 0); }
		public TerminalNode NEQ() { return getToken(LangParser.NEQ, 0); }
		public RelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel; }
	}

	public final RelContext rel() throws RecognitionException {
		RelContext _localctx = new RelContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_rel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(LangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(LangParser.MINUS, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		return exp(0);
	}

	private ExpContext exp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpContext _localctx = new ExpContext(_ctx, _parentState);
		ExpContext _prevctx = _localctx;
		int _startState = 58;
		enterRecursionRule(_localctx, 58, RULE_exp, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(239);
			termino(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(249);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(247);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(241);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(242);
						match(PLUS);
						setState(243);
						termino(0);
						}
						break;
					case 2:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(244);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(245);
						match(MINUS);
						setState(246);
						termino(0);
						}
						break;
					}
					} 
				}
				setState(251);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode MULT() { return getToken(LangParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(LangParser.DIV, 0); }
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		return termino(0);
	}

	private TerminoContext termino(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TerminoContext _localctx = new TerminoContext(_ctx, _parentState);
		TerminoContext _prevctx = _localctx;
		int _startState = 60;
		enterRecursionRule(_localctx, 60, RULE_termino, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(253);
			factor();
			}
			_ctx.stop = _input.LT(-1);
			setState(263);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(261);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new TerminoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_termino);
						setState(255);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(256);
						match(MULT);
						setState(257);
						factor();
						}
						break;
					case 2:
						{
						_localctx = new TerminoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_termino);
						setState(258);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(259);
						match(DIV);
						setState(260);
						factor();
						}
						break;
					}
					} 
				}
				setState(265);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(LangParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(LangParser.RPAREN, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public TerminalNode ID() { return getToken(LangParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public SignContext sign() {
			return getRuleContext(SignContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_factor);
		try {
			setState(279);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				match(LPAREN);
				setState(267);
				expresion();
				setState(268);
				match(RPAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(271);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(272);
				cte();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(273);
				sign();
				setState(274);
				match(ID);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(276);
				sign();
				setState(277);
				cte();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SignContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(LangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(LangParser.MINUS, 0); }
		public SignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign; }
	}

	public final SignContext sign() throws RecognitionException {
		SignContext _localctx = new SignContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_sign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode CTE_INT() { return getToken(LangParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(LangParser.CTE_FLOAT, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			_la = _input.LA(1);
			if ( !(_la==CTE_FLOAT || _la==CTE_INT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 29:
			return exp_sempred((ExpContext)_localctx, predIndex);
		case 30:
			return termino_sempred((TerminoContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp_sempred(ExpContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean termino_sempred(TerminoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u011e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001R\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002X\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004c\b"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006k\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0003\bz\b\b\u0001\t\u0001\t\u0003"+
		"\t~\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u0089\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u0093\b\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u009c\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00ae\b\u0010\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u00b2\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0003\u0016\u00d1\b\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0019\u0001\u0019\u0003\u0019\u00dd\b\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u00e4\b\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u00eb\b\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0005\u001d"+
		"\u00f8\b\u001d\n\u001d\f\u001d\u00fb\t\u001d\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0005\u001e\u0106\b\u001e\n\u001e\f\u001e\u0109\t\u001e\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0003\u001f\u0118\b\u001f\u0001 \u0001 \u0001!\u0001!\u0001!\u0000\u0002"+
		":<\"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*,.02468:<>@B\u0000\u0004\u0001\u0000\u0005\u0006"+
		"\u0001\u0000\u0014\u0016\u0001\u0000\u0010\u0011\u0001\u0000 !\u0118\u0000"+
		"D\u0001\u0000\u0000\u0000\u0002Q\u0001\u0000\u0000\u0000\u0004W\u0001"+
		"\u0000\u0000\u0000\u0006Y\u0001\u0000\u0000\u0000\bb\u0001\u0000\u0000"+
		"\u0000\nd\u0001\u0000\u0000\u0000\fj\u0001\u0000\u0000\u0000\u000el\u0001"+
		"\u0000\u0000\u0000\u0010y\u0001\u0000\u0000\u0000\u0012}\u0001\u0000\u0000"+
		"\u0000\u0014\u0088\u0001\u0000\u0000\u0000\u0016\u008a\u0001\u0000\u0000"+
		"\u0000\u0018\u0092\u0001\u0000\u0000\u0000\u001a\u009b\u0001\u0000\u0000"+
		"\u0000\u001c\u009d\u0001\u0000\u0000\u0000\u001e\u00a2\u0001\u0000\u0000"+
		"\u0000 \u00ad\u0001\u0000\u0000\u0000\"\u00b1\u0001\u0000\u0000\u0000"+
		"$\u00b3\u0001\u0000\u0000\u0000&\u00b9\u0001\u0000\u0000\u0000(\u00bd"+
		"\u0001\u0000\u0000\u0000*\u00c5\u0001\u0000\u0000\u0000,\u00d0\u0001\u0000"+
		"\u0000\u0000.\u00d2\u0001\u0000\u0000\u00000\u00d5\u0001\u0000\u0000\u0000"+
		"2\u00dc\u0001\u0000\u0000\u00004\u00e3\u0001\u0000\u0000\u00006\u00ea"+
		"\u0001\u0000\u0000\u00008\u00ec\u0001\u0000\u0000\u0000:\u00ee\u0001\u0000"+
		"\u0000\u0000<\u00fc\u0001\u0000\u0000\u0000>\u0117\u0001\u0000\u0000\u0000"+
		"@\u0119\u0001\u0000\u0000\u0000B\u011b\u0001\u0000\u0000\u0000DE\u0005"+
		"\u0001\u0000\u0000EF\u0005#\u0000\u0000FG\u0005\u0017\u0000\u0000GH\u0003"+
		"\u0002\u0001\u0000HI\u0003\f\u0006\u0000IJ\u0005\u0002\u0000\u0000JK\u0003"+
		"\u0016\u000b\u0000KL\u0005\u0003\u0000\u0000LM\u0005\u0000\u0000\u0001"+
		"M\u0001\u0001\u0000\u0000\u0000NO\u0005\u0004\u0000\u0000OR\u0003\u0004"+
		"\u0002\u0000PR\u0001\u0000\u0000\u0000QN\u0001\u0000\u0000\u0000QP\u0001"+
		"\u0000\u0000\u0000R\u0003\u0001\u0000\u0000\u0000SX\u0003\u0006\u0003"+
		"\u0000TU\u0003\u0006\u0003\u0000UV\u0003\u0004\u0002\u0000VX\u0001\u0000"+
		"\u0000\u0000WS\u0001\u0000\u0000\u0000WT\u0001\u0000\u0000\u0000X\u0005"+
		"\u0001\u0000\u0000\u0000YZ\u0003\b\u0004\u0000Z[\u0005\u0018\u0000\u0000"+
		"[\\\u0003\n\u0005\u0000\\]\u0005\u0017\u0000\u0000]\u0007\u0001\u0000"+
		"\u0000\u0000^c\u0005#\u0000\u0000_`\u0005#\u0000\u0000`a\u0005\u0019\u0000"+
		"\u0000ac\u0003\b\u0004\u0000b^\u0001\u0000\u0000\u0000b_\u0001\u0000\u0000"+
		"\u0000c\t\u0001\u0000\u0000\u0000de\u0007\u0000\u0000\u0000e\u000b\u0001"+
		"\u0000\u0000\u0000fg\u0003\u000e\u0007\u0000gh\u0003\f\u0006\u0000hk\u0001"+
		"\u0000\u0000\u0000ik\u0001\u0000\u0000\u0000jf\u0001\u0000\u0000\u0000"+
		"ji\u0001\u0000\u0000\u0000k\r\u0001\u0000\u0000\u0000lm\u0003\u0010\b"+
		"\u0000mn\u0005#\u0000\u0000no\u0005\u001a\u0000\u0000op\u0003\u0012\t"+
		"\u0000pq\u0005\u001b\u0000\u0000qr\u0005\u001e\u0000\u0000rs\u0003\u0002"+
		"\u0001\u0000st\u0003\u0016\u000b\u0000tu\u0005\u001f\u0000\u0000uv\u0005"+
		"\u0017\u0000\u0000v\u000f\u0001\u0000\u0000\u0000wz\u0005\u0007\u0000"+
		"\u0000xz\u0003\n\u0005\u0000yw\u0001\u0000\u0000\u0000yx\u0001\u0000\u0000"+
		"\u0000z\u0011\u0001\u0000\u0000\u0000{~\u0003\u0014\n\u0000|~\u0001\u0000"+
		"\u0000\u0000}{\u0001\u0000\u0000\u0000}|\u0001\u0000\u0000\u0000~\u0013"+
		"\u0001\u0000\u0000\u0000\u007f\u0080\u0005#\u0000\u0000\u0080\u0081\u0005"+
		"\u0018\u0000\u0000\u0081\u0089\u0003\n\u0005\u0000\u0082\u0083\u0005#"+
		"\u0000\u0000\u0083\u0084\u0005\u0018\u0000\u0000\u0084\u0085\u0003\n\u0005"+
		"\u0000\u0085\u0086\u0005\u0019\u0000\u0000\u0086\u0087\u0003\u0014\n\u0000"+
		"\u0087\u0089\u0001\u0000\u0000\u0000\u0088\u007f\u0001\u0000\u0000\u0000"+
		"\u0088\u0082\u0001\u0000\u0000\u0000\u0089\u0015\u0001\u0000\u0000\u0000"+
		"\u008a\u008b\u0005\u001c\u0000\u0000\u008b\u008c\u0003\u0018\f\u0000\u008c"+
		"\u008d\u0005\u001d\u0000\u0000\u008d\u0017\u0001\u0000\u0000\u0000\u008e"+
		"\u008f\u0003\u001a\r\u0000\u008f\u0090\u0003\u0018\f\u0000\u0090\u0093"+
		"\u0001\u0000\u0000\u0000\u0091\u0093\u0001\u0000\u0000\u0000\u0092\u008e"+
		"\u0001\u0000\u0000\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0093\u0019"+
		"\u0001\u0000\u0000\u0000\u0094\u009c\u0003\u001c\u000e\u0000\u0095\u009c"+
		"\u0003*\u0015\u0000\u0096\u009c\u0003(\u0014\u0000\u0097\u009c\u0003."+
		"\u0017\u0000\u0098\u009c\u0003\u001e\u000f\u0000\u0099\u009c\u0003$\u0012"+
		"\u0000\u009a\u009c\u0003&\u0013\u0000\u009b\u0094\u0001\u0000\u0000\u0000"+
		"\u009b\u0095\u0001\u0000\u0000\u0000\u009b\u0096\u0001\u0000\u0000\u0000"+
		"\u009b\u0097\u0001\u0000\u0000\u0000\u009b\u0098\u0001\u0000\u0000\u0000"+
		"\u009b\u0099\u0001\u0000\u0000\u0000\u009b\u009a\u0001\u0000\u0000\u0000"+
		"\u009c\u001b\u0001\u0000\u0000\u0000\u009d\u009e\u0005#\u0000\u0000\u009e"+
		"\u009f\u0005\u000f\u0000\u0000\u009f\u00a0\u00036\u001b\u0000\u00a0\u00a1"+
		"\u0005\u0017\u0000\u0000\u00a1\u001d\u0001\u0000\u0000\u0000\u00a2\u00a3"+
		"\u0005\b\u0000\u0000\u00a3\u00a4\u0005\u001a\u0000\u0000\u00a4\u00a5\u0003"+
		" \u0010\u0000\u00a5\u00a6\u0005\u001b\u0000\u0000\u00a6\u00a7\u0005\u0017"+
		"\u0000\u0000\u00a7\u001f\u0001\u0000\u0000\u0000\u00a8\u00ae\u0003\"\u0011"+
		"\u0000\u00a9\u00aa\u0003\"\u0011\u0000\u00aa\u00ab\u0005\u0019\u0000\u0000"+
		"\u00ab\u00ac\u0003 \u0010\u0000\u00ac\u00ae\u0001\u0000\u0000\u0000\u00ad"+
		"\u00a8\u0001\u0000\u0000\u0000\u00ad\u00a9\u0001\u0000\u0000\u0000\u00ae"+
		"!\u0001\u0000\u0000\u0000\u00af\u00b2\u00036\u001b\u0000\u00b0\u00b2\u0005"+
		"\"\u0000\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b1\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b2#\u0001\u0000\u0000\u0000\u00b3\u00b4\u0005\r\u0000"+
		"\u0000\u00b4\u00b5\u0005\u001a\u0000\u0000\u00b5\u00b6\u0005#\u0000\u0000"+
		"\u00b6\u00b7\u0005\u001b\u0000\u0000\u00b7\u00b8\u0005\u0017\u0000\u0000"+
		"\u00b8%\u0001\u0000\u0000\u0000\u00b9\u00ba\u0005\u000e\u0000\u0000\u00ba"+
		"\u00bb\u00036\u001b\u0000\u00bb\u00bc\u0005\u0017\u0000\u0000\u00bc\'"+
		"\u0001\u0000\u0000\u0000\u00bd\u00be\u0005\u000b\u0000\u0000\u00be\u00bf"+
		"\u0005\u001a\u0000\u0000\u00bf\u00c0\u00036\u001b\u0000\u00c0\u00c1\u0005"+
		"\u001b\u0000\u0000\u00c1\u00c2\u0005\f\u0000\u0000\u00c2\u00c3\u0003\u0016"+
		"\u000b\u0000\u00c3\u00c4\u0005\u0017\u0000\u0000\u00c4)\u0001\u0000\u0000"+
		"\u0000\u00c5\u00c6\u0005\t\u0000\u0000\u00c6\u00c7\u0005\u001a\u0000\u0000"+
		"\u00c7\u00c8\u00036\u001b\u0000\u00c8\u00c9\u0005\u001b\u0000\u0000\u00c9"+
		"\u00ca\u0003\u0016\u000b\u0000\u00ca\u00cb\u0003,\u0016\u0000\u00cb\u00cc"+
		"\u0005\u0017\u0000\u0000\u00cc+\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005"+
		"\n\u0000\u0000\u00ce\u00d1\u0003\u0016\u000b\u0000\u00cf\u00d1\u0001\u0000"+
		"\u0000\u0000\u00d0\u00cd\u0001\u0000\u0000\u0000\u00d0\u00cf\u0001\u0000"+
		"\u0000\u0000\u00d1-\u0001\u0000\u0000\u0000\u00d2\u00d3\u00030\u0018\u0000"+
		"\u00d3\u00d4\u0005\u0017\u0000\u0000\u00d4/\u0001\u0000\u0000\u0000\u00d5"+
		"\u00d6\u0005#\u0000\u0000\u00d6\u00d7\u0005\u001a\u0000\u0000\u00d7\u00d8"+
		"\u00032\u0019\u0000\u00d8\u00d9\u0005\u001b\u0000\u0000\u00d91\u0001\u0000"+
		"\u0000\u0000\u00da\u00dd\u00034\u001a\u0000\u00db\u00dd\u0001\u0000\u0000"+
		"\u0000\u00dc\u00da\u0001\u0000\u0000\u0000\u00dc\u00db\u0001\u0000\u0000"+
		"\u0000\u00dd3\u0001\u0000\u0000\u0000\u00de\u00e4\u00036\u001b\u0000\u00df"+
		"\u00e0\u00036\u001b\u0000\u00e0\u00e1\u0005\u0019\u0000\u0000\u00e1\u00e2"+
		"\u00034\u001a\u0000\u00e2\u00e4\u0001\u0000\u0000\u0000\u00e3\u00de\u0001"+
		"\u0000\u0000\u0000\u00e3\u00df\u0001\u0000\u0000\u0000\u00e45\u0001\u0000"+
		"\u0000\u0000\u00e5\u00eb\u0003:\u001d\u0000\u00e6\u00e7\u0003:\u001d\u0000"+
		"\u00e7\u00e8\u00038\u001c\u0000\u00e8\u00e9\u0003:\u001d\u0000\u00e9\u00eb"+
		"\u0001\u0000\u0000\u0000\u00ea\u00e5\u0001\u0000\u0000\u0000\u00ea\u00e6"+
		"\u0001\u0000\u0000\u0000\u00eb7\u0001\u0000\u0000\u0000\u00ec\u00ed\u0007"+
		"\u0001\u0000\u0000\u00ed9\u0001\u0000\u0000\u0000\u00ee\u00ef\u0006\u001d"+
		"\uffff\uffff\u0000\u00ef\u00f0\u0003<\u001e\u0000\u00f0\u00f9\u0001\u0000"+
		"\u0000\u0000\u00f1\u00f2\n\u0002\u0000\u0000\u00f2\u00f3\u0005\u0010\u0000"+
		"\u0000\u00f3\u00f8\u0003<\u001e\u0000\u00f4\u00f5\n\u0001\u0000\u0000"+
		"\u00f5\u00f6\u0005\u0011\u0000\u0000\u00f6\u00f8\u0003<\u001e\u0000\u00f7"+
		"\u00f1\u0001\u0000\u0000\u0000\u00f7\u00f4\u0001\u0000\u0000\u0000\u00f8"+
		"\u00fb\u0001\u0000\u0000\u0000\u00f9\u00f7\u0001\u0000\u0000\u0000\u00f9"+
		"\u00fa\u0001\u0000\u0000\u0000\u00fa;\u0001\u0000\u0000\u0000\u00fb\u00f9"+
		"\u0001\u0000\u0000\u0000\u00fc\u00fd\u0006\u001e\uffff\uffff\u0000\u00fd"+
		"\u00fe\u0003>\u001f\u0000\u00fe\u0107\u0001\u0000\u0000\u0000\u00ff\u0100"+
		"\n\u0002\u0000\u0000\u0100\u0101\u0005\u0012\u0000\u0000\u0101\u0106\u0003"+
		">\u001f\u0000\u0102\u0103\n\u0001\u0000\u0000\u0103\u0104\u0005\u0013"+
		"\u0000\u0000\u0104\u0106\u0003>\u001f\u0000\u0105\u00ff\u0001\u0000\u0000"+
		"\u0000\u0105\u0102\u0001\u0000\u0000\u0000\u0106\u0109\u0001\u0000\u0000"+
		"\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001\u0000\u0000"+
		"\u0000\u0108=\u0001\u0000\u0000\u0000\u0109\u0107\u0001\u0000\u0000\u0000"+
		"\u010a\u010b\u0005\u001a\u0000\u0000\u010b\u010c\u00036\u001b\u0000\u010c"+
		"\u010d\u0005\u001b\u0000\u0000\u010d\u0118\u0001\u0000\u0000\u0000\u010e"+
		"\u0118\u00030\u0018\u0000\u010f\u0118\u0005#\u0000\u0000\u0110\u0118\u0003"+
		"B!\u0000\u0111\u0112\u0003@ \u0000\u0112\u0113\u0005#\u0000\u0000\u0113"+
		"\u0118\u0001\u0000\u0000\u0000\u0114\u0115\u0003@ \u0000\u0115\u0116\u0003"+
		"B!\u0000\u0116\u0118\u0001\u0000\u0000\u0000\u0117\u010a\u0001\u0000\u0000"+
		"\u0000\u0117\u010e\u0001\u0000\u0000\u0000\u0117\u010f\u0001\u0000\u0000"+
		"\u0000\u0117\u0110\u0001\u0000\u0000\u0000\u0117\u0111\u0001\u0000\u0000"+
		"\u0000\u0117\u0114\u0001\u0000\u0000\u0000\u0118?\u0001\u0000\u0000\u0000"+
		"\u0119\u011a\u0007\u0002\u0000\u0000\u011aA\u0001\u0000\u0000\u0000\u011b"+
		"\u011c\u0007\u0003\u0000\u0000\u011cC\u0001\u0000\u0000\u0000\u0014QW"+
		"bjy}\u0088\u0092\u009b\u00ad\u00b1\u00d0\u00dc\u00e3\u00ea\u00f7\u00f9"+
		"\u0105\u0107\u0117";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}