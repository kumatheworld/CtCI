from collections import UserList
from enum import Enum, auto
from itertools import permutations
from typing import Optional
from unittest import TestCase, main

import numpy as np


class Direction(Enum):
    BOTTOM = auto()
    RIGHT = auto()

    def __str__(self) -> str:
        return super().__str__().split(".")[-1][0]


class Grid(UserList):
    def __init__(self, width: int, height: int, prob_o: float):
        self.width = width
        self.height = height
        self.data = (np.random.rand(height, width) > prob_o).tolist()

    def __str__(self) -> str:
        return "\n".join("".join("OX"[c] for c in row) for row in self)

    def accepts(self, route: tuple[Direction, ...]) -> bool:
        if not self[0][0]:
            return False

        i = j = 0
        for d in route:
            match d:
                case Direction.BOTTOM:
                    i += 1
                case Direction.RIGHT:
                    j += 1
            if not self[i][j]:
                return False
        return True

    def is_connected(self) -> bool:
        routes = permutations(
            [Direction.BOTTOM] * (self.height - 1)
            + [Direction.RIGHT] * (self.width - 1)
        )
        return any(self.accepts(route) for route in routes)


def solve(g: Grid) -> Optional[tuple[Direction, ...]]:
    w = g.width
    h = g.height
    routes: list[Optional[list[Direction]]] = [None] * w
    for i in range(h):
        r = None
        for j in range(w):
            if g[i][j]:
                if r is None:
                    if (rj := routes[j]) is not None:
                        rj.append(Direction.BOTTOM)
                        r = rj
                else:
                    r.append(Direction.RIGHT)
                    routes[j] = r
            else:
                routes[j] = None
    return None if (r := routes[-1]) is None else tuple(r)


class TestSolution(TestCase):
    def test(self) -> None:
        pass

if __name__ == "__main__":
    main()
