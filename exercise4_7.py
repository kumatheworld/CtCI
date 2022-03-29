from typing import Optional
from unittest import TestCase, main

from common import T


class CircularDependencyException(Exception):
    pass


def solve(ps: list[T], ds: list[tuple[T, T]]) -> Optional[list[T]]:
    l = len(ps)
    d = dict(zip(ps, range(l)))
    edges = [set() for _ in range(l)]
    for s, t in ds:
        edges[d[s]].add(d[t])

    order = []
    ok = [False] * l
    ng = [False] * l

    def dfs(u: int) -> None:
        if ng[u]:
            raise CircularDependencyException
        if ok[u]:
            return
        ng[u] = True
        for v in edges[u]:
            dfs(v)
        ng[u] = False
        ok[u] = True
        order.append(u)

    while True:
        try:
            node = ok.index(False)
        except ValueError:
            return [ps[x] for x in order]
        try:
            dfs(node)
        except CircularDependencyException:
            return None


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data: list[tuple[list[str], list[tuple[str, str]]]] = [
            ([], []),
            (["o"], []),
            (["t", "h", "e"], [("h", "t"), ("e", "t"), ("e", "h")]),
            (["c", "o", "d", "e"], [("o", "e"), ("d", "o"), ("c", "e"), ("o", "c")]),
            (
                ["a", "b", "c", "d", "e", "f"],
                [
                    ("d", "a"),
                    ("b", "f"),
                    ("d", "b"),
                    ("a", "f"),
                    ("c", "d"),
                ],
            ),
        ]
        for x, y in data:
            z = solve(x, y)
            self.assertIsNotNone(z)
            for s, t in y:
                self.assertGreater(z.index(s), z.index(t))

    def test_neg(self) -> None:
        data = [
            ([0, 1], [(0, 1), (1, 0)]),
            ([2, 0, 1], [(0, 2), (1, 0), (2, 1)]),
            ([3, 2, 4, 1, 5, 0], [(4, 3), (1, 5), (5, 0), (3, 1), (0, 4), (2, 3)]),
        ]
        for x, y in data:
            self.assertIsNone(solve(x, y))


if __name__ == "__main__":
    main()
