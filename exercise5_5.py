from unittest import TestCase, main


def solve(n: int) -> bool:
    """
    For a given integer n, n & (n - 1) == 0 holds iff n is either 0 or a power of 2.
    """
    return n & (n - 1) == 0


class TestSolution(TestCase):
    def test(self) -> None:
        self.assertTrue(solve(0))
        for n in range(1, 100000):
            self.assertEqual(solve(n), bin(n).count("1") == 1)


if __name__ == "__main__":
    main()
