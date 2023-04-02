from heapq import nsmallest
from random import choices, randrange
from unittest import TestCase, main


def solve(k: int, l: list[int]) -> list[int]:
    return []


class TestSolution(TestCase):
    def test(self) -> None:
        n = 1000
        for i in range(n):
            k = randrange(i + 1)
            l = choices(range(i), k=i)
            self.assertEqual(solve(k, l), nsmallest(k, l))


if __name__ == "__main__":
    main()
