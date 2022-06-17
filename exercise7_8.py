from enum import IntEnum


class Square(IntEnum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def __str__(self) -> str:
        return ".xo"[self]
