from tempfile import TemporaryFile
from typing import Optional, TextIO
from unittest import TestCase, main

import numpy as np


def solve(f: TextIO, max_int_digits=32) -> Optional[int]:
    missing = np.full(1 << max_int_digits, True)

    for line in f:
        i = int(line)
        missing[i] = False

    idx = np.argmax(missing)
    return idx.item() if idx or missing[0] else None


class TestSolution(TestCase):
    def test(self) -> None:
        it = 100
        max_int_digits = 4
        max_elem = 1 << max_int_digits
        size = 2 * max_elem
        with TemporaryFile("w+") as f:
            for _ in range(it):
                x = np.random.randint(max_elem, size=size)
                np.savetxt(f, x, fmt="%d")
                f.seek(0)
                idx = solve(f, max_int_digits)
                if len(set(x)) == max_elem:
                    self.assertIsNone(idx)
                else:
                    self.assertNotIn(idx, x)


if __name__ == "__main__":
    main()
