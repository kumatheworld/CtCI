from copy import copy
from random import getrandbits
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree


def solve(t1: BinaryTree[CT], t2: BinaryTree[CT]) -> bool:
    return False


class TestSolution(TestCase):
    def test_pos(self) -> None:
        t1 = BinaryTree[bool]()
        for _ in range(100):
            t1.random_insert(bool(getrandbits(1)))
        t2 = BinaryTree[bool]()
        for _ in range(10):
            t2.random_insert(bool(getrandbits(1)))
        node = t1.get_random_node()
        if getrandbits(1):
            node.left = copy(t2)
        else:
            node.right = copy(t2)
        self.assertTrue(solve(t1, t2))

    def test_neg(self) -> None:
        pass


if __name__ == "__main__":
    main()
