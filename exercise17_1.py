from random import randrange
from unittest import TestCase, main


def solve(x: int, y: int) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        n = 1000
        for _ in range(it):
            x = randrange(-n, n)
            y = randrange(-n, n)
            self.assertEqual(solve(x, y), x + y)


if __name__ == "__main__":
    main()
