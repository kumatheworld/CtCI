from typing import Generic, Optional

from common import T


class AdjListGraph:
    def __init__(self, edges: list[set[int]]) -> None:
        self.edges = edges

    @classmethod
    def from_string(cls, str_edges: str) -> "AdjListGraph":
        edges = [set(int(v) for v in s.split()) for s in str_edges.split(";")]
        return cls(edges)


class Node(Generic[T]):
    def __init__(
        self,
        data: T,
        left: Optional["Node[T]"] = None,
        right: Optional["Node[T]"] = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right
