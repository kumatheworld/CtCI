from random import sample
from typing import Optional
from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, Node


def solve(n: Node[CT]) -> Optional[Node[CT]]:
    data = n.data
    succ = None

    if p := n.parent:
        if p.data > data:
            succ = p
        elif (pp := p.parent) and pp.data > data:
            succ = pp

    if nr := n.right:
        node = nr.root
        if succ is None or succ.data > node.data:
            succ = node
        while node := node.left.root:
            if (nd := node.data) < data:
                break
            if nd < succ.data:
                succ = node

    return succ


class TestSolution(TestCase):
    def test(self) -> None:
        for k in range(1, 100):
            l = sample(range(1000), k)
            d = l[0]
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
