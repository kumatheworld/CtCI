from dataclasses import dataclass, field
from enum import Enum


class State(Enum):
    EMPTY = None
    BLACK = False
    WHITE = True

    def __str__(self) -> str:
        return "." if self.value is None else "xo"[self.value]

    def opposite(self) -> "State":
        return self if self.value is None else State(not self.value)


@dataclass
class Square:
    state: State = State.EMPTY

    def __str__(self) -> str:
        return str(self.state)


@dataclass
class Othello:
    board: list[list[Square]] = field(init=False)

    def __post_init__(self) -> None:
        board = [[Square()] * 8 for _ in range(8)]
        board[3][3] = Square(State.WHITE)
        board[3][4] = Square(State.BLACK)
        board[4][3] = Square(State.BLACK)
        board[4][4] = Square(State.WHITE)
        self.board = board

    def __str__(self) -> str:
        return "\n".join("".join(str(square) for square in row) for row in self.board)
