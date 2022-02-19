from random import randrange
from unittest import TestCase, main

from common import T
from exercise2 import LinkedList


def solve(ll: LinkedList[T], k: int) -> T:
    node = ll.head
    runner = node
    for _ in range(k + 1):
        node = node.next
    while node is not None:
        node = node.next
        runner = runner.next
    return runner.data


class TestSolution(TestCase):
    def test(self) -> None:
        s = "kumatheworld"
        ll = LinkedList(s)
        k = randrange(len(s))
        data = solve(ll, k)
        self.assertEqual(data, s[k])


if __name__ == "__main__":
    main()
