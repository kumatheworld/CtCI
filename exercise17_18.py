from itertools import combinations_with_replacement
from random import choices, randrange
from unittest import TestCase, main


def solve(s: set[int], l: list[int]) -> tuple[int, int]:
    return (0, 0)


class TestSolution(TestCase):
    def test(self) -> None:
        n = 100
        for i in range(1, n):
            l = choices(range(i), k=i)
            s = set(choices(l, k=randrange(1, i + 1)))
            shortest = i
            for j, k in combinations_with_replacement(range(i), 2):
                m = l[j : k + 1]
                if s.issubset(m):
                    shortest = min(shortest, k - j)
            st, ed = solve(s, l)
            self.assertEqual(ed - st, shortest)
            self.assertTrue(s.issubset(l[st : ed + 1]))


if __name__ == "__main__":
    main()
