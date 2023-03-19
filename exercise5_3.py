from itertools import pairwise
from unittest import TestCase, main


def solve(x: int) -> int:
    y = [len(z) for z in f"{x:b}".split("0")]
    if len(y) == 1:
        return y[0]
    return max([a + b for a, b in pairwise(y)]) + 1


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0b0, 1),
            (0b1, 1),
            (0b10, 2),
            (0b101, 3),
            (0b111, 3),
            (0b1001001001, 2),
            (0b11011101111, 8),
        ]
        for x, s in data:
            self.assertEqual(solve(x), s)


if __name__ == "__main__":
    main()
    main()
