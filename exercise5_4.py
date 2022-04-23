from typing import Optional
from unittest import TestCase, main


def solve(x: int) -> tuple[int, Optional[int]]:
    return x, x

class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0b1, 0b10, None),
            (0b10, 0b100, 0b1),
            (0b11, 0b101, None),
            (0b1011, 0b1101, 0b111),
            (0b110010, 0b110100, 0b110001),
            (0b101011010111, 0b101011011011, 0b101011001111),
        ]
        for x, s in data:
            self.assertEqual(solve(x), s)


if __name__ == "__main__":
    main()
