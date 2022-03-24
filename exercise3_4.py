from collections import deque
from typing import Generic

from common import T


class BiStackQueue(Generic[T]):
    def __init__(self) -> None:
        self.s0 = deque[T]()
        self.s1 = deque[T]()

    def __repr__(self) -> str:
        return f"(s0={self.s0}, s1={self.s1}"

    def enque(self, item: T) -> None:
        self.s0.append(item)

    def deque(self) -> T:
        if not (s1 := self.s1):
            if not (s0 := self.s0):
                raise IndexError("pop from empty queue")
            while s0:
                s1.append(s0.pop())
        return s1.pop()
