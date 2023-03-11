from collections import Counter
from pprint import pprint
from random import randrange
from unittest import TestCase, main


def solve(m: int, l: list[int]) -> list[int]:
    # Maybe not the most efficient way
    l_ = l.copy()
    n = len(l_)
    k = []
    for i in range(n - 1, n - m - 1, -1):
        k.append(l_.pop(randrange(i)))
    return k


class TestSolution(TestCase):
    def test(self) -> None:
        it = 10000
        n = 5
        m = 2
        l = list(range(n))
        c = Counter()
        for _ in range(it):
            k = solve(m, l)
            c[tuple(k)] += 1
        pprint(c)


if __name__ == "__main__":
    main()
