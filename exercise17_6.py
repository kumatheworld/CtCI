from unittest import TestCase, main


def solve(n: int) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        m = 1_000_000
        count = 0
        for n in range(m):
            count += str(n).count("2")
            self.assertEqual(solve(n), count)


if __name__ == "__main__":
    main()
