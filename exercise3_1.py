from typing import Generic, Optional

from common import T


class TriStackArray(Generic[T]):
    def __init__(self, size: int = 0) -> None:
        p1_base = 2 * size // 3
        self.p1_base = p1_base
        self.p0 = 0
        self.p1 = p1_base
        self.p2 = p1_base + 1
        self.size = size
        self.array: list[Optional[T]] = [None] * size

    def __repr__(self) -> str:
        a = self.array
        return (
            f"{[a[i] for i in range(0, self.p0, 1)]}, "
            f"{[a[i] for i in range(self.p1_base, self.p1, -1)]}, "
            f"{[a[i] for i in range(self.p1_base + 1, self.p2, 1)]}"
        )

    def push0(self, item: T) -> None:
        if self.p0 > self.p1:
            raise MemoryError("stack overflow")
        self.array[self.p0] = item
        self.p0 += 1

    def push1(self, item: T) -> None:
        if self.p0 > self.p1:
            raise MemoryError("stack overflow")
        self.array[self.p1] = item
        self.p1 -= 1

    def push2(self, item: T) -> None:
        if self.p2 >= self.size:
            raise MemoryError("stack overflow")
        self.array[self.p2] = item
        self.p2 += 1

    def pop0(self) -> T:
        if self.p0 <= 0:
            raise IndexError("pop from empty stack")
        self.p0 -= 1
        return self.array[self.p0]

    def pop1(self) -> T:
        if self.p1 >= self.p1_base:
            raise IndexError("pop from empty stack")
        self.p1 += 1
        return self.array[self.p1]

    def pop2(self) -> T:
        if self.p2 <= self.p1_base + 1:
            raise IndexError("pop from empty stack")
        self.p2 -= 1
        return self.array[self.p2]
