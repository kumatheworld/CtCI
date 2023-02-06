from random import choices, randrange
from unittest import TestCase, main


def solve(l: list[int]) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        iter = 1000
        m = 10
        p = range(-m, m)
        for _ in range(iter):
            k = randrange(m)
            l = choices(p, k=k)
            s = 0
            for i in range(k):
                for j in range(i + 1, k + 1):
                    s = max(s, sum(l[i:j]))
            self.assertEqual(solve(l), s)


if __name__ == "__main__":
    main()
