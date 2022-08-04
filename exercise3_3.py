from collections import deque
from typing import Generic

from common import T


class SetOfStacks(Generic[T]):
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.stacks = deque[deque[T]]([deque()])

    def __str__(self) -> str:
        return str(self.stacks)

    def push(self, item: T) -> None:
        stack = self.stacks[-1]
        stack.append(item)
        if len(stack) == self.max_size:
            self.stacks.append(deque())

    def pop(self) -> T:
        if not (stack := self.stacks[-1]):
            try:
                self.stacks.pop()
                stack = self.stacks[-1]
            except IndexError:
                raise IndexError("pop from empty set of stacks")
        return stack.pop()
