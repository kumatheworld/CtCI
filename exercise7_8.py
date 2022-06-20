from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


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
