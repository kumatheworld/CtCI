from collections import UserList
from enum import Enum, auto
from typing import Optional
from unittest import TestCase, main

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


class Grid(UserList):
    def __init__(self, width: int, height: int, prob_o: float):
        self.width = width
        self.height = height
        self.data = [
            [Cell(c) for c in row] for row in np.random.rand(height, width) > prob_o
        ]

    def __str__(self) -> str:
        return "\n".join("".join(str(c) for c in row) for row in self)

    def accepts(self, route: tuple[Direction, ...]) -> bool:
        if self[0][0] == Cell.X:
            return False

        i = j = 0
        for d in route:
            match d:
                case Direction.BOTTOM:
                    i += 1
                case Direction.RIGHT:
                    j += 1
            if self[i][j] == Cell.X:
                return False
        return True

def solve(g: Grid) -> Optional[list[Direction]]:
    return []


class TestSolution(TestCase):
    def test(self) -> None:
        pass

if __name__ == "__main__":
    main()
