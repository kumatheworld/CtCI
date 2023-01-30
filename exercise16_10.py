from itertools import groupby
from operator import itemgetter
from unittest import TestCase, main

from numpy.random import randint


def solve(p: list[tuple[int, int]], birth_year_max: int) -> int:
    q = []
    for b, d in p:
        if b <= birth_year_max:
            q.append((b, 1))
            if d < birth_year_max:
                q.append((d + 1, -1))
    q.sort()

    r = groupby(q, itemgetter(0))
    alive = 0
    alive_max = 0
    year_max = 0
    for y, g in r:
        alive += sum(w for _, w in g)
        if alive > alive_max:
            alive_max = alive
            year_max = y

    return year_max


class TestSolution(TestCase):
    def test(self) -> None:
        age_max = 150
        birth_year_min = 1900
        birth_year_max = 2000
        n = 100
        it = 100
        for _ in range(it):
            births = randint(birth_year_min, birth_year_max, n)
            p = [(b, b + randint(age_max)) for b in births]

            alive_max = 0
            year_max = []
            for y in range(birth_year_min, birth_year_max + age_max + 1):
                alive = sum(1 for b, d in p if b <= y <= d)
                if alive == alive_max:
                    year_max.append(y)
                elif alive > alive_max:
                    alive_max = alive
                    year_max = [y]

            self.assertIn(solve(p, birth_year_max), year_max)


if __name__ == "__main__":
    main()
