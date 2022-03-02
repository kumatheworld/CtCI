from unittest import TestCase, main

from exercise2 import LinkedList, Node


def solve(node: Node) -> None:
    nn = node.next
    node.data = nn.data
    node.next = nn.next


class TestSolution(TestCase):
    def test(self) -> None:
        for s in ("you", "welcome", "to", "kumatheworld"):
            ll = LinkedList(s)
            m = len(s) // 2
            node = ll.head
            for _ in range(m, len(s) - 1):
                node = node.next
            solve(node)
            ll_gt = LinkedList(s[:m] + s[m + 1 :])
            self.assertEqual(ll, ll_gt)


if __name__ == "__main__":
    main()
