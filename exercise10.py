from bisect import bisect_left
from typing import Optional

from common import CT


def binary_search(a: list[CT], x: int, lo: int = 0, hi: Optional[int] = None) -> int:
    idx = bisect_left(a, x, lo, hi)
    if idx < len(a) and a[idx] == x:
        return idx
    raise ValueError(f"{x} is not in list")
