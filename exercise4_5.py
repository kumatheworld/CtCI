from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, BinaryTree


def solve(t: BinaryTree[CT]) -> bool:
    return t.is_binary_search_tree()


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = ["", "kumatheworld", "Cracking the Coding Interview"]
        for s in data:
            t = BinarySearchTree[str]()
            for c in s:
                t.insert(c)
            self.assertTrue(solve(t))

    def test_neg(self) -> None:
        t = BinarySearchTree[str]()
        for c in "kumatheworld":
            t.insert(c)
        t.root.right.left.right.data = "n"
        self.assertFalse(solve(t))

        t = BinarySearchTree[str]()
        for c in "Cracking the Coding Interview":
            t.insert(c)
        t.root.right.left.right.right.left.left.data = "q"
        self.assertFalse(solve(t))


if __name__ == "__main__":
    main()
