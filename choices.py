import enum


class OperationEnum(enum.Enum):
    NUMBER = 0
    SUM = 1
    SUB = 2
    DIV = 3
    MULTI = 4


class TokenTypeEnum(enum.Enum):
    NUMBER = 0
    SUM = 1
    SUB = 2
    DIV = 3
    MULTI = 4

    VAR = 5
    ATTR = 6

    OPEN_BRACKET = 8
    CLOSE_BRACKET = 9

    PRINT = 10
    EOL = 98  # semicolon
    EOF = 99
    INVALID = -1
