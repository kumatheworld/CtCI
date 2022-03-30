from random import choice, sample
from typing import Optional
from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, Node


def solve(n: Node[CT]) -> Optional[Node[CT]]:
    data = n.data
    succ = None

    node = n
    if nr := n.right:
        node = nr.root
        succ = node
        while node := node.left.root:
            succ = node
    else:
        while node := node.parent:
            if node.data > data:
                succ = node
                break

    return succ


class TestSolution(TestCase):
    def test(self) -> None:
        for k in range(1, 100):
            l = sample(range(1000), k)
            d = choice(l)
            t = BinarySearchTree[int]()
            for z in l:
                t.insert(z)
            x = t.find(d)
            s = sorted(l)
            i = s.index(d)
            y = t.find(s[i + 1]) if i < k - 1 else None
            t.root.point_parent()
            self.assertEqual(solve(x), y)


if __name__ == "__main__":
    main()
