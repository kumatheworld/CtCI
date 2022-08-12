from enum import Enum, auto


class Cell(Enum):
    O = auto()
    X = auto()

    def __str__(self) -> str:
        return super().__str__()[-1]


class Direction(Enum):
    BOTTOM = auto()
    RIGHT = auto()

    def __str__(self) -> str:
        return super().__str__().split(".")[-1][0]
