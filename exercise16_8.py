from unittest import TestCase, main


def solve(n: int) -> str:
    return ""


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0, "Zero"),
            (12, "Twelve"),
            (43, "Forty Three"),
            (56, "Fifty Six"),
            (789, "Seven Hundred Eighty Nine"),
            (1234, "One Thousand, Two Hundred Thirty Four"),
        ]
        for n, s in data:
            self.assertEqual(solve(n), s)


if __name__ == "__main__":
    main()
