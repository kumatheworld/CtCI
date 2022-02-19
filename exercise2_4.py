from itertools import takewhile
from random import choices
from unittest import TestCase, main

from common import CT
from exercise2 import LinkedList


def solve(ll: LinkedList[CT], x: CT) -> None:
    node = ll.head
    if node is None:
        return

    head = node
    tail = node

    while node is not None:
        node_next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = node_next

    ll.head = head
    tail.next = None


class TestSolution(TestCase):
    def test(self) -> None:
        data = (([], 0), ([1, 2], 3), ([9, 8], 7), (choices(range(10), k=20), 5))
        for l, x in data:
            ll = LinkedList(l)
            solve(ll, x)
            l.sort()
            self.assertEqual(sorted(ll), l)
            self.assertEqual(
                sorted(takewhile(lambda y: y < x, ll)), [y for y in l if y < x]
            )


if __name__ == "__main__":
    main()
