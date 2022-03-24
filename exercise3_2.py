from collections import deque
from typing import Generic

from common import CT


class MinStack(Generic[CT]):
    def __init__(self) -> None:
        self.stack = deque[CT]()
        self.mins = deque[CT]()

    def __len__(self) -> int:
        return len(self.stack)

    def __repr__(self) -> str:
        return f"stack={repr(self.stack)}, min={self.min()}" if self else "Empty"

    def push(self, item: CT) -> None:
        if not self or item < self.min():
            self.mins.append(item)
        self.stack.append(item)

    def pop(self) -> CT:
        if not self:
            raise IndexError("pop from empty stack")
        if (item := self.stack.pop()) == self.mins[-1]:
            self.mins.pop()
        return item

    def min(self) -> CT:
        if not self:
            raise IndexError("min from empty stack")
        return self.mins[-1]
