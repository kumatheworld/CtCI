from copy import copy
from random import getrandbits
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree


def solve(t1: BinaryTree[CT], t2: BinaryTree[CT]) -> bool:
    return False


class TestSolution(TestCase):
    def test_pos(self) -> None:
        for i in range(10):
            t1 = BinaryTree[bool]()
            for _ in range(10000):
                t1.random_insert(bool(getrandbits(1)))
            t2 = BinaryTree[bool]()
            for _ in range(i):
                t2.random_insert(bool(getrandbits(1)))
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
                t1.random_insert(getrandbits(1))
            t2 = BinaryTree[int]()
            for _ in range(i):
                t2.random_insert(getrandbits(1))
            node = t1.get_random_node()
            if getrandbits(1):
                node.left = copy(t2)
            else:
                node.right = copy(t2)
            t2.random_insert(2)
            self.assertFalse(solve(t1, t2))


if __name__ == "__main__":
    main()
