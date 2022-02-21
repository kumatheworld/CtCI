from collections import deque
from typing import Generic

from common import CT


class MinStack(Generic[CT]):
    def __init__(self) -> None:
        self.stack = deque[CT]()
        self.id_min = deque[tuple[int, CT]]()

    def __len__(self) -> int:
        return len(self.stack)

    def __repr__(self) -> str:
        return f"stack={repr(self.stack)}, min={self.min()}" if self else "Empty"

    def push(self, item: CT) -> None:
        if not self or item < self.min():
            self.id_min.append((len(self), item))
        self.stack.append(item)

    def pop(self) -> CT:
        if not self:
            raise IndexError("pop from empty stack")
        item = self.stack.pop()
        if len(self) == self.id_min[-1][0]:
            self.id_min.pop()
        return item

    def min(self) -> CT:
        if not self:
            raise IndexError("min from empty stack")
        return self.id_min[-1][1]
