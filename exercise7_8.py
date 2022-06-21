from dataclasses import dataclass, field
from enum import Enum
from typing import Literal, Optional, TypeAlias


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


Coordinate: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
Point: TypeAlias = tuple[Coordinate, Coordinate]


@dataclass
class Othello:
    board: list[list[Square]] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        board = [[Square()] * 8 for _ in range(8)]
        board[3][3] = Square(Color.WHITE)
        board[3][4] = Square(Color.BLACK)
        board[4][3] = Square(Color.BLACK)
        board[4][4] = Square(Color.WHITE)
        self.board = board

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
