from random import choices
from unittest import TestCase, main

from common import T
from exercise2 import LinkedList


def solve(ll: LinkedList[T]) -> None:
    seen = set()  # is set the best?
    node = ll.head
    if node is not None:
        runner = node
    while node is not None:
        if node.data in seen:
            runner.next = node.next
        else:
            seen.add(node.data)
            runner = node
        node = node.next


class TestSolution(TestCase):
    def test(self) -> None:
        l = choices(range(10), k=20)
        ll = LinkedList(l)
        solve(ll)
        s = set(l)
        self.assertEqual(len(ll), len(s))
        self.assertEqual(set(ll), s)


if __name__ == "__main__":
    main()
