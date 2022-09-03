from math import comb
from unittest import TestCase, main

from common import CT, T
from exercise4 import BinarySearchTree


def solve(t: BinarySearchTree[CT]) -> list[list[CT]]:
    def merge_in_order(x: list[T], y: list[T]) -> list[list[T]]:
        if x == []:
            return [y]
        if y == []:
            return [x]
        xx = [[*z, x[-1]] for z in merge_in_order(x[:-1], y)]
        yy = [[*z, y[-1]] for z in merge_in_order(x, y[:-1])]
        return xx + yy

    if t:
        root = t.root
        l = solve(root.left)
        r = solve(root.right)
        d = root.data
        c = []
        for x in l:
            for y in r:
                c.extend([[d, *z] for z in merge_in_order(x, y)])
        return c
    return [[]]


def count(t: BinarySearchTree) -> tuple[int, int]:
    if t:
        root = t.root
        nl, cl = count(root.left)
        nr, cr = count(root.right)
        return 1 + nl + nr, cl * cr * comb(nl + nr, nl)
    else:
        return 0, 1


class TestSolution(TestCase):
    def test(self) -> None:
        s = "kumatheworld"
        t = BinarySearchTree[str]()
        for i in s:
            t.insert(i)

        ls = solve(t)
        self.assertEqual(len(ls), count(t)[1])
        u = []
        for l in ls:
            self.assertNotIn(l, u)
            u.append(l)
            v = BinarySearchTree[str]()
            for x in l:
                v.insert(x)
            self.assertEqual(v, t)


if __name__ == "__main__":
    main()
