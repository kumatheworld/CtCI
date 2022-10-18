from collections import Counter
from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase, main

import numpy as np


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
            stream = StringIO()
            with redirect_stdout(stream):
                solve(a)
            output = [int(s) for s in stream.getvalue().split()]
            cnt = Counter(a)
            dup = {k for k, v in cnt.items() if v > 1}
            assert set(output) == dup


if __name__ == "__main__":
    main()
