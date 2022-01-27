from unittest import TestCase, main

from exercise2 import LinkedList


def solve(ll: LinkedList) -> bool:
    kk = LinkedList()
    for data in ll:
        kk.append(data)
    return kk == ll


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = ("", "a", "ee", "lol", "noon", "madam", "123454323454321")
        for s in data:
            ll = LinkedList(s)
            self.assertTrue(solve(ll))

    def test_neg(self) -> None:
        data = ("ab", "zoo", "adam", "kumatheworld")
        for s in data:
            ll = LinkedList(s)
            self.assertFalse(solve(ll))


if __name__ == "__main__":
    main()
