from dataclasses import dataclass, field
from typing import TypeAlias

Edge: TypeAlias = int


@dataclass
class Piece:
    edges: tuple[Edge, Edge, Edge, Edge]

    def rotate(self, n: int) -> None:
        edges = self.edges
        self.edges = edges[n:] + edges[:n]


@dataclass
class JigsawPuzzle:
    width: int
    height: int
    pieces: list[Piece] = field(init=False)

    def __post_init__(self) -> None:
        w = self.width
        h = self.height
        num_horizontal_edges = w * (h - 1)
        num_vertical_edges = (w - 1) * h
        num_edges = num_horizontal_edges + num_vertical_edges
        edges = random.sample(range(1, num_edges + 1), num_edges)
        eh = edges[num_vertical_edges:]
        ev = edges[:num_vertical_edges]
        self.pieces = [
            Piece(
                (
                    0 if i == 0 else eh[(i - 1) * h + j],
                    0 if j == 0 else ev[i * h + (j - 1)],
                    0 if i == h - 1 else eh[i * h + j],
                    0 if j == w - 1 else ev[i * h + j],
                )
            )
            for i in range(h)
            for j in range(w)
        ]
