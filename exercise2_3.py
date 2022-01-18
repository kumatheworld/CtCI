from unittest import TestCase, main

from exercise2 import LinkedList, T


def solve(ll: LinkedList[T]) -> None:
    node = ll.head
    if node is None:
        raise IndexError("pop from empty list")

    node = node.next
    if node is None:
        ll.head = None
        return

    node = node.next
    runner = ll.head
    while node is not None:
        node = node.next
        if node is None:
            break
        node = node.next
        runner = runner.next
    runner.next = runner.next.next


class TestSolution(TestCase):
    def test_pos(self) -> None:
        for s in ("o", "you", "welcome", "to", "kumatheworld"):
            ll = LinkedList(s)
            solve(ll)
            k = len(s)
            m = k // 2
            if k % 2 == 0:
                ll_gts = (
                    LinkedList(s[: m - 1] + s[m:]),
                    LinkedList(s[:m] + s[m + 1 :]),
                )
                self.assertIn(ll, ll_gts)
            else:
                ll_gt = LinkedList(s[:m] + s[m + 1 :])
                self.assertEqual(ll, ll_gt)

    def test_neg(self) -> None:
        ll = LinkedList()
        with self.assertRaises(IndexError):
            solve(ll)


if __name__ == "__main__":
    main()
