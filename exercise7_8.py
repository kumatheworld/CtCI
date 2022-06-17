from dataclasses import dataclass, field
from enum import IntEnum


class Square(IntEnum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def __str__(self) -> str:
        return ".xo"[self]


@dataclass
class Othello:
    board: list[list[Square]] = field(init=False)

    def __post_init__(self) -> None:
        board = [[Square.EMPTY] * 8 for _ in range(8)]
        board[3][3] = Square.WHITE
        board[3][4] = Square.BLACK
        board[4][3] = Square.BLACK
        board[4][4] = Square.WHITE
        self.board = board

    def __str__(self) -> str:
        return "\n".join("".join(str(square) for square in row) for row in self.board)
