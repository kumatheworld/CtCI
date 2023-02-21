from itertools import chain, combinations
from random import choices, randrange
from unittest import TestCase, main


def solve(l: list[int], s: int) -> list[list[int]]:
    return []


class TestSolution(TestCase):
    def test(self) -> None:
        it = 10
        n = 10
        rng = range(-n, n)
        for _ in range(it):
            l = choices(rng, k=randrange(n))
            s = randrange(n)
            powerset = chain.from_iterable(
                combinations(l, i) for i in range(len(l) + 1)
            )
            m = sorted(k for k in powerset if sum(k) == s)
            self.assertEqual(sorted(solve(l, s)), m)


if __name__ == "__main__":
    main()
