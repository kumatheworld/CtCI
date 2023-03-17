from random import shuffle
from unittest import TestCase, main


class MissingArray:
    def __init__(self, i: int, n: int) -> None:
        a = list(range(n + 1))
        del a[i]
        shuffle(a)
        self._a = a

    def query(self, i: int, j: int) -> int:
        return (self._a[i] >> j) & 1


def solve(a: MissingArray) -> int:
    l = a._a
    return (len(l) * (len(l) + 1)) // 2 - sum(l)


class TestSolution(TestCase):
    def test(self) -> None:
        m = 100
        for n in range(m):
            for i in range(n + 1):
                a = MissingArray(i, n)
                self.assertEqual(solve(a), i)


if __name__ == "__main__":
    main()
