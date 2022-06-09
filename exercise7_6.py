import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TypeAlias
from unittest import TestCase, main

Edge: TypeAlias = int
flat: Edge = 0


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
                    flat if i == 0 else eh[(i - 1) * w + j],
                    flat if j == 0 else ev[i * (w - 1) + (j - 1)],
                    flat if i == h - 1 else eh[i * w + j],
                    flat if j == w - 1 else ev[i * (w - 1) + j],
                )
            )
            for i in range(h)
            for j in range(w)
        ]

    def rotate90deg(self) -> None:
        w = self.width
        h = self.height
        self.width = h
        self.height = w
        self_pieces = self.pieces
        pieces = [
            self_pieces[j + i] for j in range(w - 1, -1, -1) for i in range(0, w * h, w)
        ]
        for p in pieces:
            p.rotate(3)
        self.pieces = pieces

    def eq(self, pieces: list[Piece]) -> bool:
        for _ in range(4):
            if pieces == self.pieces:
                return True
            self.rotate90deg()
        return False


class Solver(ABC):
    @abstractmethod
    def solve(self, pieces: list[Piece]) -> None:
        pass


class TestSolution(TestCase):
    def test(self) -> None:
        width = 8
        height = 6
        jp = JigsawPuzzle(width, height)
        pieces = random.sample(jp.pieces, width * height)
        for p in pieces:
            p.rotate(random.randrange(4))
        solver = Solver()
        solver.solve(pieces)
        self.assertTrue(jp.eq(pieces))


if __name__ == "__main__":
    main()
