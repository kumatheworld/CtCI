from itertools import product
from random import choices, randrange
from typing import Optional
from unittest import TestCase, main


def solve(a: list[int], b: list[int]) -> Optional[tuple[int, int]]:
    return None


class TestSolution(TestCase):
    def test(self) -> None:
        iter = 100
        n = 1000
        p = range(-n, n)

        for _ in range(iter):
            l = randrange(n)
            m = randrange(n)
            a = choices(p, k=l)
            b = choices(p, k=m)

            sa = sum(a)
            sb = sum(b)
            diff = sb - sa
            for x, y in product(a, b):
                if 2 * (y - x) == diff:
                    z = solve(a, b)
                    self.assertIsNotNone(z)
                    i, j = z
                    self.assertIn(i, a)
                    self.assertIn(j, b)
                    self.assertEqual(sa + 2 * j, sb + 2 * i)
                    break
            else:
                self.assertIsNone(solve(a, b))


if __name__ == "__main__":
    main()
