import enum


class OperationEnum(enum.Enum):
    NUMBER = 0
    SUM = 1
    SUB = 2


class TokenTypeEnum(enum.Enum):
    NUMBER = 0
    SUM = 1
    SUB = 2

    VAR = 3

    PRINT = 4
    EOF = 99
    INVALID = -1
