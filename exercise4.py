from collections import deque
from typing import Generic, Iterator, Optional

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
        self.left = BinaryTree[CT](left)
        self.right = BinaryTree[CT](right)

    def point_parent(self) -> None:
        self.parent = None
        if left := self.left:
            node = left.root
            node.point_parent()
            node.parent = self
        if right := self.right:
            node = right.root
            node.point_parent()
            node.parent = self


class BinaryTree(Generic[CT]):
    def __init__(self, root=None) -> None:
        self.root: Optional[Node[CT]] = root

    def __bool__(self) -> bool:
        return self.root is not None

    def __repr__(self) -> str:
        trees = deque[BinaryTree[CT]]((self,))
        r3pr = ""
        cnt = 1
        while trees:
            if cnt == 0:
                r3pr += "\n"
                cnt = len(trees)
            if tree := trees.popleft():
                node = tree.root
                r3pr += f"{node.data } "
                trees.extend((node.left, node.right))
            else:
                r3pr += "* "
            cnt -= 1
        return r3pr

    def __iter__(self) -> Iterator["Node[CT]"]:
        trees = deque[BinaryTree[CT]]((self,))
        while trees:
            if tree := trees.popleft():
                node = tree.root
                yield node
                trees.append(node.left)
                trees.append(node.right)

    def insert(self, data: CT) -> None:
        if self:
            root = self.root
            tree = root.left if data < root.data else root.right
            tree.insert(data)
        else:
            self.root = Node(data)

    def find(self, data: CT) -> Optional[Node[CT]]:
        if self:
            root = self.root
            if data == (rd := root.data):
                return root
            elif data < rd:
                return root.left.find(data)
            else:
                return root.right.find(data)
        return None

    def height(self) -> int:
        if self:
            root = self.root
            hl = root.left.height()
            hr = root.right.height()
            return max(hl, hr) + 1
        return 0

    def in_range(self, a: Optional[CT], b: Optional[CT]) -> bool:
        if self:
            root = self.root
            data = root.data
            return (
                (a is None or a <= data)
                and (b is None or data <= b)
                and root.left.in_range(a, data)
                and root.right.in_range(data, b)
            )
        return True

    def is_binary_search_tree(self) -> bool:
        return self.in_range(None, None)


class BinarySearchTree(BinaryTree[CT]):
    pass
