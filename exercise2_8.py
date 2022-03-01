from random import choices, randrange
from unittest import TestCase, main

from common import T
from exercise2 import LinkedList, Node


# what a beautiful solution! how could one come up with this?
def solve(x: LinkedList[T]) -> Node[T]:
    runner = x.head.next
    node = runner.next
    while runner is not node:
        runner = runner.next
        node = node.next.next

    runner = x.head
    while runner is not node:
        runner = runner.next
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
