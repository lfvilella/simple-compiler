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
        '=': Token(choices.TokenTypeEnum.ATTR),
        '(': Token(choices.TokenTypeEnum.OPEN_BRACKET),
        ')': Token(choices.TokenTypeEnum.CLOSE_BRACKET),
        ';': Token(choices.TokenTypeEnum.EOL),
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

        if peek.startswith('$'):
            variable = ''
            while peek not in self.DATA_TYPES.keys():
                variable += peek
                peek = self._next_char()

            self.position -= 1
            return Token(choices.TokenTypeEnum.VAR, variable)

        if peek.startswith('p'):
            print_ = ''
            while peek != '(':
                print_ += peek
                peek = self._next_char()

            self.position -= 1
            return Token(choices.TokenTypeEnum.PRINT, print_)

        if str.isdigit(peek):
            value = ''
            while str.isdigit(peek) or peek == '.':
                value += peek
                peek = self._next_char()

            self.position -= 1
            return Token(choices.TokenTypeEnum.NUMBER, float(value))

        return self.DATA_TYPES.get(peek, Token(choices.TokenTypeEnum.INVALID))
