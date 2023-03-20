from contextlib import suppress
from random import choices
from string import ascii_letters, digits
from unittest import TestCase, main


def solve(l: list[str]) -> list[str]:
    return l


class TestSolution(TestCase):
    def test(self) -> None:
        charset = ascii_letters + digits
        n = 1000
        for k in range(n):
            l = choices(charset, k=k)
            y = []
            for i in range(k):
                m = []
                for h, j in enumerate(range(i, k + 1, 2)):
                    if len([s for s in m if s.isdigit()]) == h:
                        y.append(m.copy())
                    with suppress(IndexError):
                        m += (l[j], l[j + 1])
            x = solve(l)
            self.assertEqual(len(x), max(len(m) for m in y))
            self.assertIn(x, y)


if __name__ == "__main__":
    main()
