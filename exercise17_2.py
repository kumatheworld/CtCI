from collections import Counter
from pprint import pprint
from random import randrange
from unittest import TestCase, main


def solve(l: list) -> None:
    # Maybe not the most efficient way
    n = len(l)
    for i in range(n - 1, 0, -1):
        l.append(l.pop(randrange(i)))


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
