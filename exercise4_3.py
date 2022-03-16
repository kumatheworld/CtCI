from collections import deque
from unittest import TestCase, main

from common import CT
from exercise4 import BinarySearchTree, Node


def solve(t: BinarySearchTree[CT]) -> list[deque[Node[CT]]]:
    if t.root is None:
        return []
    l = []
    cnt = 0
    q = deque[Node[CT]]((t.root,))
    while q:
        if cnt == 0:
            l.append(q.copy())
            cnt = len(q)
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        cnt -= 1
    return l


class TestSolution(TestCase):
    # just look at the printed tree and solution!
    def test(self) -> None:
        s = "CrackingTheCodingInterview"
        t = BinarySearchTree[str]()
        for i in s:
            t.insert(i)
        print(t)
        print([[node.data for node in q] for q in solve(t)])


if __name__ == "__main__":
    main()
