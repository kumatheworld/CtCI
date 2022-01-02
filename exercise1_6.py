from itertools import groupby
from unittest import TestCase, main


def solve(s: str) -> str:
    t = "".join(x[0] + str(len(list(x[1]))) for x in groupby(s))
    return t if len(t) < len(s) else s


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            ("aabcccccaaa", "a2b1c5a3"),
            ("ohhhhhhhhh i see", "o1h9 1i1 1s1e2"),
            ("aabb", "aabb"),
            ("mississippi", "mississippi"),
        ]
        for s, t in data:
            self.assertEqual(solve(s), t)


if __name__ == "__main__":
    main()
