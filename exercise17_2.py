from collections import Counter
from pprint import pprint
from random import shuffle
from unittest import TestCase, main


def solve(l: list) -> None:
    shuffle(l)


class TestSolution(TestCase):
    def test(self) -> None:
        it = 10000
        n = 4
        l = list(range(n))
        c = Counter()
        for _ in range(it):
            solve(l)
            c[tuple(l)] += 1
        pprint(c)


if __name__ == "__main__":
    main()
