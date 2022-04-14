from random import choice, sample
from typing import Optional
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree, Node


def solve(x: Node[CT], y: Node[CT], t: BinaryTree[CT]) -> Node[CT]:
    # this is effectively storing intermediate nodes though...
    def path2(
        z: Node[CT], t_: BinaryTree[CT], path: list[bool]
    ) -> Optional[list[bool]]:
        if t_:
            root = t_.root
            if root == z:
                return path
            if p4th := path2(z, root.left, path + [False]):
                return p4th
            else:
                return path2(z, root.right, path + [True])
        return None

    px = path2(x, t, [])
    py = path2(y, t, [])
    i = 0
    m = min(len(px), len(py))
    node = t.root
    while i < m and (b := px[i]) == py[i]:
        node = node.right.root if b else node.left.root
        i += 1

    return node


def ancestors(node: Node[CT]) -> list[Node[CT]]:
    anc = [node]
    while node := node.parent:
        anc.append(node)
    return anc[::-1]


class TestSolution(TestCase):
    def test(self) -> None:
        for k in range(1, 100):
            l = sample(range(k), k)
            t = BinaryTree[int]()
            for z in l:
                t.insert(z)
            x = t.find(choice(l))
            y = t.find(choice(l))
            z = solve(x, y, t)

            t.root.point_parent()
            ax = ancestors(x)
            ay = ancestors(y)
            m = min(len(ax), len(ay))
            i = 0
            while i < m and ax[i] == ay[i]:
                i += 1

            self.assertEqual(z, ax[i - 1])


if __name__ == "__main__":
    main()
