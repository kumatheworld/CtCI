from typing import Optional
from unittest import TestCase, main


def solve(a: int, b: int) -> Optional[int]:
    return bin(c).count("1") if (c := a ^ b) >= 0 else None


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            ((0b11101, 0b11101), 0),
            ((0b11101, 0b1111), 2),
            ((-0b11101, 0b1111), None),
            ((0b11101, -0b1111), None),
            ((-0b11101, -0b1111), 2),
            ((-0b1011000100101, -0b101001), 5),
        ]
        for (a, b), c in data:
            self.assertEqual(solve(a, b), c)


if __name__ == "__main__":
    main()
