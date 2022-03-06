from collections import deque
from unittest import TestCase, main

from exercise4 import AdjListGraph


def solve(g: AdjListGraph, s: int, t: int) -> bool:
    edges = g.edges
    seen = set((s,))
    q = deque((s,))
    while q:
        u = q.popleft()
        if u == t:
            return True
        q.extend(edges[u] - seen)
        seen.union(edges[u])
    return False


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = [
            ("", 0, 0),
            ("0", 0, 0),
            ("1;", 0, 1),
            ("1 2; 0;", 1, 2),
            ("3; 2; 3;", 1, 3),
            ("1 2 3; 0 2 3; 0 1 3; 0 1 2", 3, 0),
            ("1; 5; 4; ; 1; 0 3", 0, 3),
        ]
        for r, s, t in data:
            g = AdjListGraph.from_string(r)
            self.assertTrue(solve(g, s, t))

    def test_neg(self) -> None:
        data = [
            (";", 0, 1),
            ("1;", 1, 0),
            ("1;", 1, 0),
            ("1 2; 0;", 2, 0),
            ("3; 2; 3;", 3, 2),
            ("1; 5; 4; ; 1; 0 3", 5, 4),
        ]
        for r, s, t in data:
            g = AdjListGraph.from_string(r)
            self.assertFalse(solve(g, s, t))


if __name__ == "__main__":
    main()
