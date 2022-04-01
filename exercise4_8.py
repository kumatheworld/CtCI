from random import choice, randrange, sample
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree, Node


def solve(x: Node[CT], y: Node[CT], t: BinaryTree[CT]) -> Node[CT]:
    return x


def randomize(tree: BinaryTree[int]):
    if tree:
        root = tree.root
        root.data = randrange(100)
        randomize(root.left)
        randomize(root.right)


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
            randomize(t)
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
