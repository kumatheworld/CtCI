from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next: Optional["Node[T]"] = None):
        self.data = data
        self.next = next
