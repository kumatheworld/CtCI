from copy import copy
from random import getrandbits
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree


def solve(t1: BinaryTree[CT], t2: BinaryTree[CT]) -> bool:
    if t1 == t2:
        return True
    if not t1:
        return False
    root = t1.root
    return solve(root.left, t2) or solve(root.right, t2)


class TestSolution(TestCase):
    def test_pos(self) -> None:
        for i in range(10):
            t1 = BinaryTree[bool]()
            for _ in range(10000):
                t1.insert(bool(getrandbits(1)))
            t2 = BinaryTree[bool]()
            for _ in range(i):
                t2.insert(bool(getrandbits(1)))
            node = t1.get_random_node()
            if getrandbits(1):
                node.left = copy(t2)
            else:
                node.right = copy(t2)
            self.assertTrue(solve(t1, t2))

    def test_neg(self) -> None:
        for i in range(10):
            t1 = BinaryTree[int]()
            for _ in range(10000):
                t1.insert(getrandbits(1))
            t2 = BinaryTree[int]()
            for _ in range(i):
                t2.insert(getrandbits(1))
            node = t1.get_random_node()
            if getrandbits(1):
                node.left = copy(t2)
            else:
                node.right = copy(t2)
            t2.insert(2)
            self.assertFalse(solve(t1, t2))


if __name__ == "__main__":
    main()
