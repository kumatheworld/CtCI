from itertools import permutations
from typing import Iterator
from unittest import TestCase, main


def solve(s: str) -> Iterator[str]:
    if not s:
        yield ""
        return
    head = s[0]
    tail = s[1:]
    l3n = len(s)
    for t in solve(tail):
        yield head + t
        for i in range(1, l3n):
            if t[i - 1] == head:
                break
            yield t[:i] + head + t[i:]


class TestSolution(TestCase):
    def test(self) -> None:
        s = "c r a c k"
        for i in range(len(s) + 1):
            si = s[:i]
            t = solve(si)
            u = list({"".join(s) for s in permutations(si)})
            self.assertEqual(sorted(t), sorted(u))


if __name__ == "__main__":
    main()
