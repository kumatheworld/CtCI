from collections import deque
from typing import Generic, Optional

from common import CT, T


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

    def insert(self, data: CT) -> None:
        attr = "left" if data < self.data else "right"
        node = getattr(self, attr)
        node.insert(data) if node else setattr(self, attr, Node(data))


class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None

    def __repr__(self) -> str:
        nodes = deque[Optional[Node[T]]]((self.root,))
        r3pr = ""
        cnt = 1
        while nodes:
            if cnt == 0:
                r3pr += "\n"
                cnt = len(nodes)
            node = nodes.popleft()
            if node:
                r3pr += f"{node.data } "
                nodes.extend((node.left, node.right))
            else:
                r3pr += "* "
            cnt -= 1
        return r3pr


class BinarySearchTree(BinaryTree[CT]):
    def insert(self, data: CT) -> None:
        root = self.root
        if root is None:
            self.root = Node(data)
        else:
            root.insert(data)
