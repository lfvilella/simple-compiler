"""Simple Parser

Grammar:
    prog ::= stmt EOL lines
    lines::= prog | ε
    stmt ::= attr | imp
    attr  ::= VAR EQ expr
    imp  ::= PRINT OPEN VAR CLOSE
    expr ::= fact SUM expr | fact SUB expr | fact
    fact ::= term MULT fact | term DIV fact | term
    term ::= OPEN expr CLOSE | NUM | VAR
"""

import simple_lexer
import symbol_table
import choices


class SimpleParser:
    def __init__(self, lexer_: simple_lexer.SimpleLexer):
        self._lexer = lexer_
        self._look_ahead = self._lexer.next_token()

        self.output = ''

    def _match(self, token: simple_lexer.Token):
        if (
            self._look_ahead.type != token.type
            or self._look_ahead.attribute != token.attribute
        ):
            raise SyntaxError('Values do not match.')

        self._look_ahead = self._lexer.next_token()

    # def term(self) -> int:
    #     if self._look_ahead.type != choices.TokenTypeEnum.NUMBER:
    #         raise SyntaxError(
    #             f'The value `{self._look_ahead.attribute}` is not a number.'
    #         )

    #     value = self._look_ahead.attribute
    #     self._match(self._look_ahead)
    #     return value

    def expr(self) -> float:  # expr ::= fact SUM expr | fact SUB expr | fact
        _fact = self.fact()
        if self._look_ahead.type == choices.TokenTypeEnum.SUM:
            self._match(simple_lexer.Token(choices.TokenTypeEnum.SUM))
            _expr = self.expr()
            return _fact + _expr

        elif self._look_ahead.type == choices.TokenTypeEnum.SUB:
            self._match(simple_lexer.Token(choices.TokenTypeEnum.SUB))
            _expr = self.expr()
            return _fact - _expr

        return _fact

    def prog(self):  # prog ::= stmt EOL lines
        self.stmt()
        self._match(simple_lexer.Token(choices.TokenTypeEnum.EOL))
        self.lines()

    def lines(self):  # lines::= prog | ε
        if self._look_ahead.type != choices.TokenTypeEnum.EOF:
            self.prog()

    def stmt(self):  # stmt ::= attr | imp
        if self._look_ahead.type == choices.TokenTypeEnum.VAR:
            self.attr()
        elif self._look_ahead.type == choices.TokenTypeEnum.PRINT:
            self.imp()
        else:
            raise SyntaxError(
                f'Expected VAR or PRINT and receives {self._look_ahead.type}'
            )

    def attr(self):  # attr  ::= VAR EQ expr
        value = self._look_ahead.attribute
        self._match(simple_lexer.Token(choices.TokenTypeEnum.VAR, value))
        self._match(simple_lexer.Token(choices.TokenTypeEnum.ATTR))
        _expr = self.expr()
        symbol_table.set(value, _expr)

    def imp(self):  # imp  ::= PRINT OPEN VAR CLOSE
        self._match(simple_lexer.Token(choices.TokenTypeEnum.PRINT, 'print'))
        self._match(simple_lexer.Token(choices.TokenTypeEnum.OPEN_BRACKET))
        key = self._look_ahead.attribute
        self._match(simple_lexer.Token(choices.TokenTypeEnum.VAR, key))
        self._match(simple_lexer.Token(choices.TokenTypeEnum.CLOSE_BRACKET))
        value = symbol_table.get(key)
        print(value)

    def fact(self):  # fact ::= term MULT fact | term DIV fact | term
        _term = self.term()
        if self._look_ahead.type == choices.TokenTypeEnum.MULTI:
            self._match(simple_lexer.Token(choices.TokenTypeEnum.MULTI))
            _fact = self.fact()
            return _term * _fact

        elif self._look_ahead.type == choices.TokenTypeEnum.DIV:
            self._match(simple_lexer.Token(choices.TokenTypeEnum.DIV))
            _fact = self.fact()
            return _term / _fact

        return _term

    def term(self):  # term ::= OPEN expr CLOSE | NUM | VAR
        if self._look_ahead.type == choices.TokenTypeEnum.OPEN_BRACKET:
            return self.expr()

        elif self._look_ahead.type == choices.TokenTypeEnum.NUMBER:
            value = self._look_ahead.attribute
            self._match(
                simple_lexer.Token(choices.TokenTypeEnum.NUMBER, value)
            )
            return value

        elif self._look_ahead.type == choices.TokenTypeEnum.VAR:
            key = self._look_ahead.attribute
            self._match(simple_lexer.Token(choices.TokenTypeEnum.VAR, key))
            return symbol_table.get(key)

        raise SyntaxError(f'Unexpected symbol {self._look_ahead.attribute}')
