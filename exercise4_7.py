from typing import Optional
from unittest import TestCase, main

from common import T


def solve(ps: list[T], ds: list[tuple[T, T]]) -> Optional[list[T]]:
    return None


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data: list[tuple[list[str], list[tuple[str, str]]]] = [
            ([], []),
            (["o"], []),
            (["t", "h", "e"], [("h", "t"), ("e", "t"), ("e", "h")]),
            (["c", "o", "d", "e"], [("o", "e"), ("d", "o"), ("o", "c"), ("o", "e")]),
            (
                ["a", "b", "c", "d", "e", "f"],
                [
                    ("d", "a"),
                    ("b", "f"),
                    ("d", "b"),
                    ("a", "f"),
                    ("c", "d"),
                ],
            ),
        ]
        for x, y in data:
            z = solve(x, y)
            self.assertIsNotNone(z)
            for s, t in y:
                self.assertGreater(z.index(s), z.index(t))

    def test_neg(self) -> None:
        data = [
            ([0, 1], [(0, 1), (1, 0)]),
            ([2, 0, 1], [(0, 2), (1, 0), (2, 1)]),
            ([3, 2, 4, 1, 5, 0], [(4, 3), (1, 5), (5, 0), (3, 1), (0, 4), (2, 3)]),
        ]
        for x, y in data:
            self.assertIsNone(solve(x, y))


if __name__ == "__main__":
    main()
