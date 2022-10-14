from csv import reader
from pathlib import Path
from typing import Optional
from unittest import TestCase, main

import numpy as np


def solve(p: Path, max_int_digits=32, delimiter=",") -> Optional[int]:
    missing = np.full(1 << max_int_digits, True)
    with p.open() as f:
        ints = reader(f, delimiter=delimiter)
        for line in ints:
            for s in line:
                i = int(s)
                missing[i] = False

    idx = np.argmax(missing)
    return idx.item() if idx or missing[0] else None
