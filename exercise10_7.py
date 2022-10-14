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
