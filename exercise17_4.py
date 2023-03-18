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
    n = 0
    while True:
        try:
            a.query(n, 0)
        except IndexError:
            break
        n += 1

    if n == 0:
        return 0

    rem = list(range(n))
    log2n = n.bit_length()
    k = 0
    for j in range(log2n):
        zeros = []
        ones = []
        for i in rem:
            b = a.query(i, j)
            (ones if b else zeros).append(i)
        if len(ones) < len(zeros):
            rem = ones
            k |= 1 << j
        else:
            rem = zeros

    return k


class TestSolution(TestCase):
    def test(self) -> None:
        m = 100
        for n in range(m):
            for i in range(n + 1):
                a = MissingArray(i, n)
                self.assertEqual(solve(a), i)


if __name__ == "__main__":
    main()
