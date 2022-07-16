from dataclasses import dataclass
from enum import IntEnum
from itertools import product
from random import sample


class ExplosiveNumber(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    MINE = 9


@dataclass
class Square:
    number: ExplosiveNumber = ExplosiveNumber.ZERO
    discovered: bool = False

    def __str__(self) -> str:
        return str(int(self.number)) if self.discovered else " "


@dataclass
class MineSweeper:
    width: int
    height: int
    num_mines: int

    def __post_init__(self) -> None:
        w = self.width
        h = self.height

        mines = sample(list(product(range(h), range(w))), self.num_mines)
        board = [[0] * self.width for _ in range(self.height)]
        for x, y in mines:
            for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
                if dx != 0 or dy != 0:
                    i = x + dx
                    j = y + dy
                    if i in range(h) and j in range(w):
                        board[i][j] += 1
        for x, y in mines:
            board[x][y] = ExplosiveNumber.MINE
        self.__board = tuple(
            tuple(Square(ExplosiveNumber(board[i][j])) for j in range(w))
            for i in range(h)
        )
