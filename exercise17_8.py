from itertools import chain, combinations, pairwise, product
from random import randrange
from unittest import TestCase, main


def solve(p: list[tuple[int, int]]) -> int:
    q = [(0, 0), *sorted(p)]

    longests = [0]
    for r in q[1:]:
        l_max = 1 + max(k for s, k in zip(q, longests) if s[0] < r[0] and s[1] < r[1])
        longests.append(l_max)

    return max(longests)


class TestSolution(TestCase):
    def test(self) -> None:
        n = 10
        it = 100
        for i, _ in product(range(n), range(it)):
            ans = 0
            people = [(randrange(40, 80), randrange(50, 500)) for _ in range(n)]
            pred = solve(people)
            people.sort()
            powerset = chain.from_iterable(
                combinations(people, i) for i in range(n + 1)
            )
            for p in powerset:
                if all(b[0] < c[0] and b[1] < c[1] for b, c in pairwise(p)):
                    ans = max(ans, len(p))
            self.assertEqual(pred, ans)


if __name__ == "__main__":
    main()
