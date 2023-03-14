from collections import Counter
from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase, main

import numpy as np

from common import memory_limit


def solve(a: list[int]) -> None:
    # Is it allowed to print one value multiple times?
    # If not, just sort in-place and run through the array
    dup = np.full(32000, False)
    for i in a:
        if dup[i]:
            print(i)
        else:
            dup[i] = True


class TestSolution(TestCase):
    def test(self) -> None:
        n = np.random.randint(32000)
        size = 1000
        it = 1000
        for _ in range(it):
            a = np.random.randint(n, size=size).tolist()
            with StringIO() as f, redirect_stdout(f):
                solve(a)
                output = [int(s) for s in f.getvalue().split()]
            cnt = Counter(a)
            dup = {k for k, v in cnt.items() if v > 1}
            assert set(output) == dup

    def test_space(self) -> None:
        n = 32000
        size = 1_000_000
        a = np.random.randint(n, size=size).tolist()
        with redirect_stdout(None), memory_limit(1 << 15):
            solve(a)


if __name__ == "__main__":
    main()
