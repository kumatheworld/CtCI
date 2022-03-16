from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, BinaryTree


def solve(t: BinaryTree[CT]) -> bool:
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
