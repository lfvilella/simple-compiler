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

    PRINT = 6
    EOF = 99
    INVALID = -1
