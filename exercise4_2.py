from random import choices
from typing import Optional
from unittest import TestCase, main

from exercise4 import BinarySearchTree, Node


def solve(l: list[int]) -> BinarySearchTree[int]:
    def solve_rec(l_: list[int]) -> Optional[Node[int]]:
        if l_:
            m = len(l_) // 2
            return Node(l_[m], solve_rec(l_[:m]), solve_rec(l_[m + 1 :]))
        else:
            return None

    t = BinarySearchTree[int]()
    t.root = solve_rec(l)
    return t


class TestSolution(TestCase):
    def test(self) -> None:
        for k in range(100):
            l = sorted(choices(range(10), k=k))
            t = solve(l)
            self.assertTrue(t.is_binary_search_tree())
            self.assertEqual(t.height(), k.bit_length())


if __name__ == "__main__":
    main()
