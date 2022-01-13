from collections.abc import Iterable, Iterator
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next: Optional["Node[T]"] = None):
        self.data = data
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self, it: Iterable[T] = ()):
        self.head: Optional[Node[T]] = None
        self.extend(it)

    def __repr__(self) -> str:
        return f"LL{tuple(iter(self))[::-1]}"

    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        for d1, d2 in zip(self, other):
            if d1 != d2:
                return False
        return True

    def append(self, data: T) -> None:
        node = Node(data, self.head)
        self.head = node

    def extend(self, it: Iterable[T]) -> None:
        for data in it:
            self.append(data)

    def pop(self) -> T:
        head = self.head
        if head is None:
            raise IndexError("pop from empty list")
        data = head.data
        self.head = head.next
        return data
