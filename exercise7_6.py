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
