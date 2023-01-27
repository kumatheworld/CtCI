from unittest import TestCase, main

from numpy.random import randint


def solve(l: list[tuple[int, int]]) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        n = 10
        age_max = 150
        birth_year_min = 1900
        birth_year_max = 2000
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

        self.assertIn(solve(p), year_max)


if __name__ == "__main__":
    main()
