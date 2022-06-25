from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from itertools import product
from random import choice
from typing import Literal, Optional, TypeAlias

Coordinate: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
Point: TypeAlias = tuple[Coordinate, Coordinate]


class Color(Enum):
    BLACK = False
    WHITE = True

    def __str__(self) -> str:
        return "xo"[self.value]

    def opposite(self) -> "Color":
        return Color(not self.value)


@dataclass
class Square:
    state: Optional[Color] = None
    flippable_points: set[Point] = field(default_factory=set)

    def __str__(self) -> str:
        return "." if self.state is None else str(self.state)

    def flip(self) -> None:
        if self.state is not None:
            self.state = self.state.opposite()


class Direction(Enum):
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    SW = (-1, 1)
    W = (-1, 0)
    NW = (-1, -1)
    N = (0, -1)
    NE = (1, -1)


class Othello:
    def __init__(self) -> None:
        board = tuple(tuple(Square() for _ in range(8)) for _ in range(8))
        board[3][3].state = Color.WHITE
        board[3][4].state = Color.BLACK
        board[4][3].state = Color.BLACK
        board[4][4].state = Color.WHITE
        self.board = board
        self.turn = Color.BLACK

    def __str__(self) -> str:
        return "\n".join("".join(str(square) for square in row) for row in self.board)

    def get_flippable_squares(self, color: Color, p: Point) -> list[Square]:
        x, y = p
        board = self.board
        if board[x][y].state is not None:
            return []

        squares = []
        for d in Direction:
            dx, dy = d.value
            xx, yy = x + dx, y + dy
            ss: list[Square] = []
            while xx in range(8) and yy in range(8):
                square = board[xx][yy]
                match square.state:
                    case None:
                        break
                    case c if c is color:
                        squares.extend(ss)
                    case _:
                        ss.append(square)
                xx += dx
                yy += dy
        return squares

    def get_placeable_points(self, color: Color) -> list[Point]:
        return [
            (x, y)
            for x in range(8)
            for y in range(8)
            if self.get_flippable_squares(color, (x, y))
        ]


class Player(ABC):
    @abstractmethod
    def play(self, othello: Othello) -> Point:
        pass


class RandomPlayer(Player):
    def play(self, othello: Othello) -> Point:
        return choice(
            [
                (x, y)
                for x, y in product(range(8), range(8))
                if othello.board[x][y].flippable_points
            ]
        )
