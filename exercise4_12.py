from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree


def solve(x: int, t: BinaryTree[CT]) -> int:
    def partial_sums(t_: BinaryTree) -> tuple[list[int], list[int]]:
        if t_:
            root = t_.root
            data = root.data
            rl, ul = partial_sums(root.left)
            rr, ur = partial_sums(root.right)
            r = rl + rr
            sums_rooted = [data + s for s in r] + [data]
            sums_unrooted = ul + ur + r
            return sums_rooted, sums_unrooted
        else:
            return [], []

    sums_rooted, sums_unrooted = partial_sums(t)
    sums = sums_rooted + sums_unrooted
    return sums.count(x)


class TestSolution(TestCase):
    def test(self) -> None:
        # This is not a test! Start the debug mode and just inspect sums
        t = BinaryTree[int]()
        for i in range(7):
            t.insert(i)
        print(t)
        print(solve(5, t))


if __name__ == "__main__":
    main()
