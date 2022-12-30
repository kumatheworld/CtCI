from collections import Counter
from unittest import TestCase, main


def solve(w: str, b: list[str]) -> int:
    c = Counter(b)
    return c[w]


class TestSolution(TestCase):
    def test(self) -> None:
        with open(__file__) as f:
            b = f.read().split()
        for w in b:
            self.assertEqual(solve(w, b), sum(w_ == w for w_ in b))


if __name__ == "__main__":
    main()
