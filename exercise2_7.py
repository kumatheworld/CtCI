from random import choices, randrange
from typing import Optional
from unittest import TestCase, main

from common import T
from exercise2 import LinkedList, Node


def rev_singleton_ll(x: LinkedList[T]) -> LinkedList[tuple[Node]]:
    y = LinkedList()
    node = x.head
    while node is not None:
        y.append((node,))
        node = node.next
    return y


def solve(x: LinkedList[T], y: LinkedList[T]) -> Optional[Node[T]]:
    rx = rev_singleton_ll(x)
    ry = rev_singleton_ll(y)
    node = None
    for nx, ny in zip(rx, ry):
        if nx[0] != ny[0]:
            break
        node = nx[0]
    return node


class TestSolution(TestCase):
    def test_pos(self) -> None:
        for _ in range(10):
            lx = randrange(1, 10)
            x = LinkedList(choices(range(2), k=lx))
            ix = randrange(lx)
            nx = x.head
            for _ in range(ix):
                nx = nx.next

            ly = randrange(1, 10)
            y = LinkedList(choices(range(2), k=ly))
            iy = randrange(ly)
            ny = y.head
            for _ in range(iy):
                ny = ny.next

            nx.next = ny
            self.assertIs(solve(x, y), ny)

    def test_neg(self) -> None:
        data = (("", "kuma"), ("chan", ""), ("nitty", "gritty"))
        for sx, sy in data:
            x = LinkedList(sx)
            y = LinkedList(sy)
            self.assertIsNone(solve(x, y))


if __name__ == "__main__":
    main()
