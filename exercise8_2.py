from collections import UserList
from enum import Enum, auto

import numpy as np


class Cell(Enum):
    O = 0
    X = 1

    def __str__(self) -> str:
        return super().__str__()[-1]


class Direction(Enum):
    BOTTOM = auto()
    RIGHT = auto()

    def __str__(self) -> str:
        return super().__str__().split(".")[-1][0]


class CellMatrix(UserList):
    def __init__(self, width: int, height: int, prob_o: float):
        self.data = [
            [Cell(c) for c in row] for row in np.random.rand(height, width) > prob_o
        ]

    def __str__(self) -> str:
        return "\n".join("".join(str(c) for c in row) for row in self)
