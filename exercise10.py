from bisect import bisect_left
from typing import Optional, Sequence

from common import CT


def binary_search(a: Sequence[CT], x: CT, lo: int = 0, hi: Optional[int] = None) -> int:
    idx = bisect_left(a, x, lo, hi)
    if idx < (hi if hi else len(a)) and a[idx] == x:
        return idx
    raise ValueError(f"{x} is not in list")
