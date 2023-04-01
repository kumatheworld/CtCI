from collections import Counter
from random import choices, randrange, shuffle
from unittest import TestCase, main


def solve(l: list[int]) -> int:
    return -1


class TestSolution(TestCase):
    def test_positive(self) -> None:
        n = 1000
        for i in range(1, n):
            k = randrange(1, 2 * i)
            m = randrange(i // 2 + 1, i + 1)
            l = [k] * m + choices(range(1, 2 * i), k=i - m)
            shuffle(l)
            self.assertEqual(solve(l), k)

    def test_negative_empty(self) -> None:
        self.assertEqual(solve([]), -1)

    def test_negative_nonempty(self) -> None:
        n = 1000
        for i in range(1, n):
            l = choices(range(i + 1), k=i)
            if Counter(l).most_common(1)[0][1] <= i // 2:
                self.assertEqual(solve(l), -1)


if __name__ == "__main__":
    main()
