from itertools import takewhile
from random import choices
from unittest import TestCase, main

from exercise2 import LinkedList, T


def solve(ll: LinkedList[T], x: T) -> None:
    node = ll.head
    head_lt = None
    node_lt = None
    head_ge = None
    node_ge = None

    while node is not None:
        if node.data < x:
            if head_lt is None:
                head_lt = node
            else:
                node_lt.next = node
            node_lt = node
        else:
            if head_ge is None:
                head_ge = node
            else:
                node_ge.next = node
            node_ge = node
        node = node.next

    if node_lt is not None:
        node_lt.next = None
    if node_ge is not None:
        node_ge.next = head_lt
    ll.head = head_ge


class TestSolution(TestCase):
    def test(self) -> None:
        l = choices(range(10), k=20)
        x = 5
        ll = LinkedList(l)
        solve(ll, x)
        l.sort()
        self.assertEqual(sorted(ll), l)
        self.assertEqual(
            sorted(takewhile(lambda y: y >= x, ll)), [y for y in l if y >= x]
        )


if __name__ == "__main__":
    main()
