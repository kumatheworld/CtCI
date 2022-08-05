from collections import deque
from collections.abc import Iterator
from random import choice, choices, getrandbits
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
        self.left = BinaryTree[CT](left)
        self.right = BinaryTree[CT](right)

    def __copy__(self) -> "Node[CT]":
        return type(self)(
            self.data,
            left.root.__copy__() if (left := self.left) else None,
            right.root.__copy__() if (right := self.right) else None,
        )

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
    def __init__(self, root: Optional[Node[CT]] = None) -> None:
        self.root = root

    def __bool__(self) -> bool:
        return self.root is not None

    def _eq(self, other: "BinaryTree[CT]") -> bool:
        if not (self and other):
            return not (self or other)
        rs = self.root
        ro = other.root
        return rs.data == ro.data and rs.left._eq(ro.left) and rs.right._eq(ro.right)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self._eq(other)

    def __str__(self) -> str:
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

    def __iter__(self) -> Iterator[CT]:  # BFS
        trees = deque[BinaryTree[CT]]((self,))
        while trees:
            if tree := trees.popleft():
                node = tree.root
                yield node.data
                trees.append(node.left)
                trees.append(node.right)

    def __copy__(self) -> "BinaryTree[CT]":
        return type(self)(self.root.__copy__() if self else None)

    def insert(self, data: CT) -> None:
        if self:
            root = self.root
            tree = root.left if getrandbits(1) else root.right
            tree.insert(data)
        else:
            self.root = Node(data)

    def find(self, data: CT) -> Optional[Node[CT]]:
        trees = deque[BinaryTree[CT]]((self,))
        while trees:
            if tree := trees.popleft():
                node = tree.root
                if node.data == data:
                    return node
                trees.append(node.left)
                trees.append(node.right)
        raise ValueError(f"{data} is not in tree")

    def delete(self, data: CT) -> None:
        target = None
        trees = deque[BinaryTree[CT]]((self,))
        while trees:
            if tree := trees.popleft():
                node = tree.root
                if (node := tree.root).data == data:
                    target = tree
                    break
                trees.append(node.left)
                trees.append(node.right)
        else:
            raise ValueError(f"{data} is not in tree")
        alt = target
        while True:
            root = alt.root
            left = root.left
            right = root.right
            if left or right:
                alt = choice([t for t in (left, right) if t])
            else:
                break
        target.root.data = alt.root.data
        alt.root = None

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

    def _get_random_node_with_count(self) -> tuple[Optional[Node[CT]], int]:
        if self:
            root = self.root
            nl, cl = root.left._get_random_node_with_count()
            nr, cr = root.right._get_random_node_with_count()
            node = choices((root, nl, nr), (1, cl, cr), k=1)[0]
            count = 1 + cl + cr
            return node, count
        else:
            return None, 0

    def get_random_node(self) -> Optional[Node[CT]]:
        return self._get_random_node_with_count()[0]


class CNode(Node[CT]):
    def __init__(
        self,
        data: CT,
        left: Optional["CNode[CT]"] = None,
        right: Optional["CNode[CT]"] = None,
    ) -> None:
        self.data = data
        self.left = BinarySearchTree[CT](left)
        self.right = BinarySearchTree[CT](right)


class BinarySearchTree(BinaryTree[CT]):
    def __init__(self, root: Optional[CNode[CT]] = None) -> None:
        self.root = root

    def insert(self, data: CT) -> None:
        if self:
            root = self.root
            tree = root.left if data < root.data else root.right
            tree.insert(data)
        else:
            self.root = CNode(data)

    def find(self, data: CT) -> Optional[CNode[CT]]:
        if self:
            root = self.root
            if data == (rd := root.data):
                return root
            elif data < rd:
                return root.left.find(data)
            else:
                return root.right.find(data)
        else:
            raise ValueError(f"{data} is not in tree")
