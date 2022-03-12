from collections import deque
from typing import Generic, Optional

from common import CT


class AdjListGraph:
    def __init__(self, edges: list[set[int]]) -> None:
        self.edges = edges

    @classmethod
    def from_string(cls, str_edges: str) -> "AdjListGraph":
        edges = [set(int(v) for v in s.split()) for s in str_edges.split(";")]
        return cls(edges)


class Node(Generic[CT]):
    def __init__(
        self,
        data: CT,
        left: Optional["Node[CT]"] = None,
        right: Optional["Node[CT]"] = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def height(self) -> int:
        left = self.left
        right = self.right
        hl = 0 if left is None else left.height()
        hr = 0 if right is None else right.height()
        return max(hl, hr) + 1

    def insert(self, data: CT) -> None:
        attr = "left" if data < self.data else "right"
        node = getattr(self, attr)
        node.insert(data) if node else setattr(self, attr, Node(data))

    def in_range(self, a: Optional[CT], b: Optional[CT]) -> bool:
        data = self.data
        left = self.left
        right = self.right
        return (
            (a is None or a <= data)
            and (b is None or data <= b)
            and (left is None or left.in_range(a, data))
            and (right is None or right.in_range(data, b))
        )


class BinaryTree(Generic[CT]):
    def __init__(self) -> None:
        self.root: Optional[Node[CT]] = None

    def __repr__(self) -> str:
        nodes = deque[Optional[Node[CT]]]((self.root,))
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

    def is_binary_search_tree(self) -> bool:
        return self.root.in_range(None, None) if self.root else True


class BinarySearchTree(BinaryTree[CT]):
    def insert(self, data: CT) -> None:
        root = self.root
        if root is None:
            self.root = Node(data)
        else:
            root.insert(data)
