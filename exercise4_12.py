from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree


def solve(x: int, t: BinaryTree[CT]) -> int:
    def partial_sums(t_: BinaryTree) -> tuple[list[int], int]:
        if t_:
            root = t_.root
            data = root.data
            rl, cl = partial_sums(root.left)
            rr, cr = partial_sums(root.right)
            sums_rooted = [data + s for s in rl + rr] + [data]
            count = cl + cr + sums_rooted.count(x)
            return sums_rooted, count
        else:
            return [], 0

    return partial_sums(t)[1]


class TestSolution(TestCase):
    def test(self) -> None:
        # This is not a test! Run this multiple times and get some sense
        t = BinaryTree[int]()
        for i in range(10):
            t.insert(i)
        print(t)
        print(solve(7, t))


if __name__ == "__main__":
    main()
