from random import sample
from typing import Optional
from unittest import TestCase, main


def solve(a: list[int]) -> Optional[int]:
    def solve_(a_: list[int], offset: int) -> Optional[int]:
        if a_ == []:
            return None

        m = len(a_) // 2
        n = m + offset
        d = a_[m] - n
        if d < 0:
            return solve_(a_[m + 1 :], n + 1)
        elif d > 0:
            return solve_(a_[:m], offset)
        else:
            return n

    return solve_(a, 0)


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        l3n = 1000
        for _ in range(it):
            a = sorted(sample(range(-200, 1200), l3n))
            ids = [i for i, x in enumerate(a) if i == x]
            b = solve(a)
            if ids:
                self.assertIsNotNone(b)
                self.assertIn(b, ids)
            else:
                self.assertIsNone(b)


if __name__ == "__main__":
    main()
