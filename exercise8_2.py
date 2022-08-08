from enum import Enum


class Cell(Enum):
    O = 0
    X = 1

    def __str__(self) -> str:
        return "OX"[self.value]


class Direction(Enum):
    BOTTOM = 0
    RIGHT = 1

    def __str__(self) -> str:
        return "BR"[self.value]
