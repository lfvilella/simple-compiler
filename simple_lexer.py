import typing

import choices


class Token:
    def __init__(self, type: choices.TokenTypeEnum, value: int = None):
        self.type = type
        self.attribute = value


class SimpleLexer:
    def __init__(self, input: str):
        self.input = self._clear_spaces(input)
        self.position = -1

    def _clear_spaces(self, text: str) -> str:
        return text.replace(' ', '')

    def _next_char(self) -> typing.Optional[str]:
        self.position += 1

        if self.position == len(self.input):
            return ''

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

        if peek == '+':
            return Token(choices.TokenTypeEnum.SUM)
        elif peek == '-':
            return Token(choices.TokenTypeEnum.SUB)
        elif peek == '':
            return Token(choices.TokenTypeEnum.EOF)

        return Token(choices.TokenTypeEnum.INVALID)
