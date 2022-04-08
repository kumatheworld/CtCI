from copy import copy
from random import randrange
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree


def solve(t1: BinaryTree[CT], t2: BinaryTree[CT]) -> bool:
    return False


class TestSolution(TestCase):
    def test_pos(self) -> None:
        t1 = BinaryTree[int]()
        for _ in range(1000):
            t1.insert(randrange(100))
        t2 = BinaryTree[int]()
        for _ in range(10):
            data = randrange(100)
            t2.insert(data)
        node = t1.get_random_node()
        if randrange(2):
            node.left = copy(t2)
        else:
            node.right = copy(t2)
        self.assertTrue(solve(t1, t2))

    def test_neg(self) -> None:
        pass


if __name__ == "__main__":
    main()
