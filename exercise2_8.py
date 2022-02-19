from random import choices, randrange
from unittest import TestCase, main

from common import T
from exercise2 import LinkedList, Node


def solve(x: LinkedList[T]) -> Node[T]:
    seen = set()
    node = x.head
    while node is not None:
        nid = id(node)
        if nid in seen:
            break
        seen.add(nid)
        node = node.next
    return node


class TestSolution(TestCase):
    def test(self) -> None:
        for _ in range(10):
            l = randrange(1, 10)
            x = LinkedList(choices(range(10), k=l))
            ix = randrange(l)
            nx = x.head
            for _ in range(ix):
                nx = nx.next
            node = x.head
            while node.next is not None:
                node = node.next
            node.next = nx
            self.assertIs(solve(x), nx)


if __name__ == "__main__":
    main()
