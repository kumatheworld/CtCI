from unittest import TestCase, main


def solve(n: int, m: int, i: int, j: int) -> int:
    return (n & (-(1 << j) | ((1 << i) - 1))) | (m << i)


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            ((0b01001011110, 0b101, 3, 5), 0b01001101110),
            ((0b10000000000, 0b10011, 2, 6), 0b10001001100),
        ]
        for t, k in data:
            self.assertEqual(solve(*t), k)


if __name__ == "__main__":
    main()
