from collections import Counter
from unittest import TestCase, main

from common import CT
from exercise4 import BinaryTree, Node


def solve(t: BinaryTree[CT]) -> Node[CT]:
    return t.get_random_node()


class TestSolution(TestCase):
    # Just look at the printed counter!
    def test(self) -> None:
        t = BinaryTree[str]()
        data = "kumatheworld"
        for c in data:
            t.insert(c)
        counter = Counter([solve(t).data for _ in range(12000)])
        print(t)
        print(counter)


if __name__ == "__main__":
    main()
