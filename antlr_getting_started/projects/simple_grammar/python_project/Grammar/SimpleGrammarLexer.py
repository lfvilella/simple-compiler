# Generated from /Users/felipe/projects/simple-compiler/antlr_getting_started/projects/simple_grammar/SimpleGrammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("D\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\6\n-\n\n\r\n\16\n.\3\13\6\13\62\n\13\r\13\16")
        buf.write("\13\63\3\f\3\f\6\f8\n\f\r\f\16\f9\3\f\3\f\3\r\6\r?\n\r")
        buf.write("\r\r\16\r@\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\3\2\6\3\2\62;\4\2C\\c|\5")
        buf.write("\2\f\f\17\17\u0080\u0080\5\2\13\f\17\17\"\"\2G\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35")
        buf.write("\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2")
        buf.write("\2\17\'\3\2\2\2\21)\3\2\2\2\23,\3\2\2\2\25\61\3\2\2\2")
        buf.write("\27\65\3\2\2\2\31>\3\2\2\2\33\34\7=\2\2\34\4\3\2\2\2\35")
        buf.write("\36\7*\2\2\36\6\3\2\2\2\37 \7+\2\2 \b\3\2\2\2!\"\7\'\2")
        buf.write("\2\"\n\3\2\2\2#$\7\61\2\2$\f\3\2\2\2%&\7,\2\2&\16\3\2")
        buf.write("\2\2\'(\7/\2\2(\20\3\2\2\2)*\7-\2\2*\22\3\2\2\2+-\t\2")
        buf.write("\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\24\3\2\2")
        buf.write("\2\60\62\t\3\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2")
        buf.write("\2\2\63\64\3\2\2\2\64\26\3\2\2\2\65\67\7%\2\2\668\t\4")
        buf.write("\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3")
        buf.write("\2\2\2;<\b\f\2\2<\30\3\2\2\2=?\t\5\2\2>=\3\2\2\2?@\3\2")
        buf.write("\2\2@>\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\b\r\2\2C\32\3\2\2")
        buf.write("\2\7\2.\639@\3\b\2\2")
        return buf.getvalue()


class SimpleGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EOL = 1
    OPEN = 2
    CLOSE = 3
    MOD = 4
    DIV = 5
    MUL = 6
    SUB = 7
    ADD = 8
    NUM = 9
    VAR = 10
    COMMENTS = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "'%'", "'/'", "'*'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "EOL", "OPEN", "CLOSE", "MOD", "DIV", "MUL", "SUB", "ADD", "NUM", 
            "VAR", "COMMENTS", "WS" ]

    ruleNames = [ "EOL", "OPEN", "CLOSE", "MOD", "DIV", "MUL", "SUB", "ADD", 
                  "NUM", "VAR", "COMMENTS", "WS" ]

    grammarFileName = "SimpleGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


