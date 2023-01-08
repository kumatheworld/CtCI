from random import randrange
from unittest import TestCase, main


def solve(x: int, y: int) -> int:
    return x


class TestSolution(TestCase):
    def test(self) -> None:
        m = 1_000_000_000
        it = 1_000
        for _ in range(it):
            x = randrange(-m, m)
            y = randrange(-m, m)
            self.assertEqual(solve(x, y), max(x, y))


if __name__ == "__main__":
    main()
