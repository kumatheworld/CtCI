import re
from typing import Optional
from unittest import TestCase, main


def solve(x: int) -> tuple[int, Optional[int]]:
    b = f"{x:b}"
    next_largest = int(re.sub(r"0(1*)(0*)$", r"10\2\1", "0" + b)[:-1], 2)
    p = re.compile(r"10(1*)$")
    next_smallest = int(re.sub(r"10(1*)$", r"01\1", b), 2) if p.search(b) else None
    return next_largest, next_smallest


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0b1, (0b10, None)),
            (0b10, (0b100, 0b1)),
            (0b11, (0b101, None)),
            (0b1011, (0b1101, 0b111)),
            (0b110010, (0b110100, 0b110001)),
            (0b101011010111, (0b101011011011, 0b101011001111)),
        ]
        for x, (y, z) in data:
            self.assertEqual(solve(x), (y, z))


if __name__ == "__main__":
    main()
