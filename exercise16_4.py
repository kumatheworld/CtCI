from typing import Optional, TypeAlias
from unittest import TestCase, main

Square: TypeAlias = Optional[bool]
Line: TypeAlias = tuple[Square, Square, Square]
Board: TypeAlias = tuple[Line, Line, Line]


def solve(b: Board) -> Optional[bool]:
    indices = [
        ((0, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 2), (1, 2), (2, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
    ]
    for idx in indices:
        line = [b[i][j] for i, j in idx]
        if None in line:
            continue
        if all(line):
            return True
        if not any(line):
            return False
    return None


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (
                (
                    (True, False, False),
                    (False, False, True),
                    (False, True, True),
                ),
                False,
            ),
            (
                (
                    (True, False, False),
                    (False, False, True),
                    (True, True, True),
                ),
                True,
            ),
            (
                (
                    (True, False, False),
                    (False, False, True),
                    (None, True, True),
                ),
                None,
            ),
        ]
        for b, w in data:
            self.assertEqual(solve(b), w)


if __name__ == "__main__":
    main()
