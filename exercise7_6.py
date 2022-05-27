from dataclasses import dataclass, field


class Edge:
    pass


@dataclass
class Piece:
    left: Edge
    top: Edge
    right: Edge
    bottom: Edge


@dataclass
class Board:
    width: int
    height: int
    left: list[Edge] = field(init=False)
    top: list[Edge] = field(init=False)
    right: list[Edge] = field(init=False)
    bottom: list[Edge] = field(init=False)

    def __post_init__(self) -> None:
        self.left = [Edge() for _ in range(self.width)]
        self.top = [Edge() for _ in range(self.height)]
        self.right = [Edge() for _ in range(self.width)]
        self.bottom = [Edge() for _ in range(self.height)]
