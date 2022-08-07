from functools import cache
from unittest import TestCase, main


@cache
def solve(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return solve(n - 1) + solve(n - 2) + solve(n - 3)


class TestSolution(TestCase):
    def test_first_couple(self) -> None:
        self.assertEqual([solve(n) for n in range(4)], [1, 1, 2, 4])


if __name__ == "__main__":
    main()
