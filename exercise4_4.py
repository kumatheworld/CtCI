from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, BinaryTree, Node


class ImbalancedTreeException(Exception):
    pass


def height(node: Node[CT]) -> int:
    left = node.left
    right = node.right
    hl = 0 if left is None else height(left)
    hr = 0 if right is None else height(right)
    diff = hl - hr
    if diff < -1 or 1 < diff:
        raise ImbalancedTreeException
    return max(hl, hr) + 1


def solve(t: BinaryTree[CT]) -> bool:
    if t.root is None:
        return True
    try:
        height(t.root)
    except ImbalancedTreeException:
        return False
    return True


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = ["", "kuma", "5261473"]
        for s in data:
            t = BinarySearchTree[str]()
            for c in s:
                t.insert(c)
            self.assertTrue(solve(t))

    def test_neg(self) -> None:
        data = ["the", "world", "215463"]
        for s in data:
            t = BinarySearchTree[str]()
            for c in s:
                t.insert(c)
            self.assertFalse(solve(t))


if __name__ == "__main__":
    main()
