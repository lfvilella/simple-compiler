import simple_lexer
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

    def term(self) -> int:
        if self._look_ahead.type != choices.TokenTypeEnum.NUMBER:
            raise SyntaxError(
                f'The value `{self._look_ahead.attribute}` is not a number.'
            )

        value = self._look_ahead.attribute
        self._match(self._look_ahead)
        return value

    def expression(self) -> int:
        term = self.term()
        while self._look_ahead.type != choices.TokenTypeEnum.EOF:
            operation, value = self.rest()

            if operation == choices.OperationEnum.SUM:
                term += value
            elif operation == choices.OperationEnum.SUB:
                term -= value
            elif operation == choices.OperationEnum.DIV:
                term /= value
            elif operation == choices.OperationEnum.MULTI:
                term *= value

        return term

    def rest(self):
        if self._look_ahead.type == choices.TokenTypeEnum.SUM:
            self._match(self._look_ahead)
            term = self.term()
            return choices.OperationEnum.SUM, term

        elif self._look_ahead.type == choices.TokenTypeEnum.SUB:
            self._match(self._look_ahead)
            term = self.term()
            return choices.OperationEnum.SUB, term

        elif self._look_ahead.type == choices.TokenTypeEnum.DIV:
            self._match(self._look_ahead)
            term = self.term()
            return choices.OperationEnum.DIV, term

        elif self._look_ahead.type == choices.TokenTypeEnum.MULTI:
            self._match(self._look_ahead)
            term = self.term()
            return choices.OperationEnum.MULTI, term

        elif self._look_ahead.type == choices.TokenTypeEnum.EOF:
            return choices.TokenTypeEnum.EOF

        raise SyntaxError(f'Unexpected symbol {self._look_ahead.attribute}')
