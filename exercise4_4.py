from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, BinaryTree


class ImbalancedTreeException(Exception):
    pass


def height_ex(tree: BinaryTree[CT]) -> int:
    if tree:
        root = tree.root
        hl = height_ex(root.left)
        hr = height_ex(root.right)
        diff = hl - hr
        if diff < -1 or 1 < diff:
            raise ImbalancedTreeException
        return max(hl, hr) + 1
    return 0


def solve(t: BinaryTree[CT]) -> bool:
    try:
        height_ex(t)
        return True
    except ImbalancedTreeException:
        return False


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
