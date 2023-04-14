from itertools import islice
from math import ceil, log2
from random import sample
from unittest import TestCase, main


def solve(l: list[int]) -> int:
    if not l:
        return 0

    n = len(l) + 1
    offset = 0
    stride = 1
    digit = 0
    for digit in range(ceil(log2(n))):
        b = 1
        for i in islice(l, offset, n, stride):
            b ^= (i >> digit) & 1
        if b:  # depends on the length? i'm confused...
            offset += stride
        stride <<= 1

    print(l, offset)
    return l[offset] ^ (1 << digit)


class TestSolution(TestCase):
    def test(self) -> None:
        n = 1000
        for i in range(1, n):
            l = sample(range(i), i)
            self.assertEqual(solve(l[:-1]), l[-1])


if __name__ == "__main__":
    main()
