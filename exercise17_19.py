from random import sample
from unittest import TestCase, main


def solve(l: list[int]) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        n = 1000
        for i in range(n):
            l = sample(range(i + 1), i + 1)
            self.assertEqual(solve(l[:1]), l[-1])


if __name__ == "__main__":
    main()
