from collections import Counter
from unittest import TestCase, main


def solve(s: str) -> bool:
    c = Counter(s.replace(" ", "").lower())
    return sum(v % 2 for v in c.values()) < 2


class TestSolution(TestCase):
    def test_pos(self) -> None:
        ss = ["Tact coa", "LeV El"]
        for s in ss:
            self.assertTrue(solve(s))

    def test_neg(self) -> None:
        ss = ["Hello", "world"]
        for s in ss:
            self.assertFalse(solve(s))


if __name__ == "__main__":
    main()
