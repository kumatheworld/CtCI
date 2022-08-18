from random import sample
from typing import Optional
from unittest import TestCase, main


def solve(a: list[int]) -> Optional[int]:
    return None


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        l3n = 1000
        for _ in range(it):
            a = sample(range(-200, 1200), l3n)
            ids = [i for i, x in enumerate(a) if i == x]
            b = solve(a)
            if ids:
                self.assertIsNotNone(b)
                self.assertIn(b, ids)
            else:
                self.assertIsNone(b)


if __name__ == "__main__":
    main()
