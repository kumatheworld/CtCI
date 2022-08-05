from collections.abc import Iterator
from dataclasses import dataclass
from enum import IntEnum
from itertools import product
from random import sample
from typing import Optional


class Explosion(Exception):
    pass


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

    def __str__(self) -> str:
        return str(int(self))


@dataclass
class Square:
    number: ExplosiveNumber = ExplosiveNumber.ZERO
    discovered: bool = False

    def __str__(self) -> str:
        return str(self.number) if self.discovered else "-"


@dataclass
class MineSweeper:
    width: int
    height: int
    num_mines: int

    def _neighbors(self, x: int, y: int) -> Iterator[tuple[int, int]]:
        w = self.width
        h = self.height
        for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
            if dx != 0 or dy != 0:
                if (i := x + dx) in range(h) and (j := y + dy) in range(w):
                    yield i, j

    def __post_init__(self) -> None:
        w = self.width
        h = self.height

        mines = sample(list(product(range(h), range(w))), self.num_mines)
        board = [[0] * self.width for _ in range(self.height)]
        for x, y in mines:
            for i, j in self._neighbors(x, y):
                board[i][j] += 1
        for x, y in mines:
            board[x][y] = ExplosiveNumber.MINE
        self.__board = tuple(
            tuple(Square(ExplosiveNumber(board[i][j])) for j in range(w))
            for i in range(h)
        )

    def __str__(self) -> str:
        return "\n".join(
            "".join("-" if n is None else str(n) for n in row) for row in self.board
        )

    def __str_debug(self) -> str:
        return "\n".join("".join(str(s.number) for s in row) for row in self.__board)

    @property
    def board(self) -> tuple[tuple[Optional[ExplosiveNumber], ...], ...]:
        return tuple(
            tuple(square.number if square.discovered else None for square in row)
            for row in self.__board
        )

    def ishalfway(self) -> bool:
        return any(
            any(s for s in row if s.number != ExplosiveNumber.MINE and not s.discovered)
            for row in self.__board
        )

    def reveal(self, x: int, y: int) -> None:
        if (s := self.__board[x][y]).discovered:
            return
        if (n := s.number) == ExplosiveNumber.MINE:
            raise Explosion("BANG!")
        s.discovered = True
        if n == ExplosiveNumber.ZERO:
            for i, j in self._neighbors(x, y):
                self.reveal(i, j)


if __name__ == "__main__":
    game = MineSweeper(8, 6, 5)
    print("Start!", game, sep="\n")
    while game.ishalfway():
        x, y = (int(s) for s in input("Point x,y to reveal: ").split(","))
        game.reveal(x, y)
        print(game)
    print("Congrats!")
