import typing

import choices


class Token:
    def __init__(self, type: choices.TokenTypeEnum, value: int = None):
        self.type = type
        self.attribute = value


class SimpleLexer:
    DATA_TYPES = {
        '+': Token(choices.TokenTypeEnum.SUM),
        '-': Token(choices.TokenTypeEnum.SUB),
        '/': Token(choices.TokenTypeEnum.DIV),
        '*': Token(choices.TokenTypeEnum.MULTI),
        'EOF': Token(choices.TokenTypeEnum.EOF),
    }

    def __init__(self, input: str):
        self.input = self._clear_spaces(input)
        self.position = -1

    def _clear_spaces(self, text: str) -> str:
        return text.replace(' ', '')

    def _next_char(self) -> typing.Optional[str]:
        self.position += 1

        if self.position == len(self.input):
            return 'EOF'

        return self.input[self.position]

    def next_token(self) -> Token:
        peek = self._next_char()
        if str.isdigit(peek):
            value = ''
            while str.isdigit(peek):
                value += peek
                peek = self._next_char()

            self.position -= 1
            return Token(choices.TokenTypeEnum.NUMBER, int(value))

        return self.DATA_TYPES.get(peek, Token(choices.TokenTypeEnum.INVALID))
