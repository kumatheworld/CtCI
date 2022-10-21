import heapq
from bisect import bisect_right
from collections import UserList

from common import CT


class RankedSequence(UserList[CT]):
    def track(self, x: CT) -> None:
        heapq.heappush(self.data, x)

    def get_rank(self, x: CT) -> int:
        idx = bisect_right(self.data, x) - 1
        if idx < 0 or self.data[idx] != x:
            raise ValueError(f"{x} is not in sequence")
        return idx
