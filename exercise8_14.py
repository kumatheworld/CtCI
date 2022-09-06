from unittest import TestCase, main


def solve(s: str, b: bool) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        data = [(("1^0|0|1", False), 2), (("0&0&0&1^1|0", True), 10)]
        for (s, b), c in data:
            self.assertEqual(solve(s, b), c)


if __name__ == "__main__":
    main()
