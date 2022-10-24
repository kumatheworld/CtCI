from collections import Counter
from random import choices
from typing import Optional
from unittest import TestCase, main

from common import CT


def solve(l: list[CT]) -> None:
    pass


class TestSolution(TestCase):
    def assertIsAlternating(
        self, l: list[CT], start: int = 0, le: Optional[bool] = None
    ) -> None:
        try:
            y = l[start + 1]
        except IndexError:
            pass
        else:
            x = l[start]
            if le is None:
                if x < y:
                    self.assertIsAlternating(l, start + 1, False)
                elif x > y:
                    self.assertIsAlternating(l, start + 1, True)
                else:
                    self.assertIsAlternating(l, start + 1, None)
            else:
                if x != y:
                    self.assertEqual(x < y, le)
                self.assertIsAlternating(l, start + 1, not le)

    def test(self) -> None:
        it = 1000
        size = 100
        for _ in range(it):
            l = choices(range(size), k=size)
            k = l.copy()
            solve(l)
            self.assertEqual(Counter(k), Counter(l))
            self.assertIsAlternating(l)


if __name__ == "__main__":
    main()
