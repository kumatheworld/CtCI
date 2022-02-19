from collections.abc import Iterable, Iterator
from itertools import zip_longest
from typing import Generic, Optional

from common import T


class Node(Generic[T]):
    def __init__(self, data: T, next: Optional["Node[T]"] = None) -> None:
        self.data = data
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self, it: Iterable[T] = ()) -> None:
        self.head: Optional[Node[T]] = None
        self.extend(it)

    def __repr__(self) -> str:
        return f"LL{tuple(iter(self))[::-1]}"

    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len([_ for _ in self])
        # the following results in infinite recursion
        # return len(list(self))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LinkedList) and all(
            x == y for x, y in zip_longest(self, other, fillvalue=object())
        )

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


class BiNode(Generic[T]):
    def __init__(
        self,
        data: T,
        prev: Optional["BiNode[T]"] = None,
        next: Optional["BiNode[T]"] = None,
    ) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(Generic[T]):
    def __init__(self, it: Iterable[T] = ()) -> None:
        self.head: Optional[BiNode[T]] = None
        self.tail: Optional[BiNode[T]] = None
        self.extend(it)

    def __repr__(self) -> str:
        return f"DLL{tuple(iter(self))[::-1]}"

    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len([_ for _ in self])

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LinkedList) and all(
            x == y for x, y in zip_longest(self, other, fillvalue=object())
        )

    def append(self, data: T) -> None:
        head = self.head
        node = BiNode(data, next=head)
        if head is None:
            self.tail = node
        else:
            head.prev = node
        self.head = node

    def appendleft(self, data: T) -> None:
        tail = self.tail
        node = BiNode(data, prev=tail)
        if tail is None:
            self.head = node
        else:
            tail.next = node
        self.tail = node

    def extend(self, it: Iterable[T]) -> None:
        for data in it:
            self.append(data)

    def extendleft(self, it: Iterable[T]) -> None:
        for data in it:
            self.appendleft(data)

    def pop(self) -> T:
        head = self.head
        if head is None:
            raise IndexError("pop from empty list")
        data = head.data
        self.head = head.next
        head = self.head
        if head is not None:
            head.prev = None
        return data

    def popleft(self) -> T:
        tail = self.tail
        if tail is None:
            raise IndexError("pop from empty list")
        data = tail.data
        self.tail = tail.prev
        tail = self.tail
        if tail is not None:
            tail.next = None
        return data
