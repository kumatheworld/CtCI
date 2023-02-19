from random import choices, getrandbits
from unittest import TestCase, main


class Ant:
    def __init__(self) -> None:
        self.radius = 0
        center = bool(getrandbits(1))
        self._squares_org = [[center]]
        self._squares = [[center]]

    def __str__(self) -> str:
        return self._str(org=False)

    def _str(self, org: bool) -> str:
        # Could be faster by bypassing __getitem__
        colors = "xo"
        rng = range(-self.radius, self.radius + 1)
        squares = self._squares_org if org else self._squares
        l = []
        for i in rng:
            row = []
            for j in rng:
                r, t = self._translate_indices(i, j)
                row.append(colors[squares[r][t]])
            l.append("".join(row))
        return "\n".join(l)

    def _translate_indices(self, i: int, j: int) -> tuple[int, int]:
        #  0 ~ 2r-1: ( n,  n) ... (-n+1, n)
        # 2r ~ 4r-1: (-n,  n) ... (-n, -n+1)
        # 4r ~ 6r-1: (-n, -n) ... (n-1, -n)
        # 6r ~ 8r-1: ( n, -n) ... ( n, n-1)
        r = max(abs(i), abs(j))
        if i <= j:
            if j == r:
                t = r - i
            else:
                t = 3 * r - j
        else:
            if j == -r:
                t = 5 * r + i
            else:
                t = 7 * r + j
        return r, t

    def _expand(self) -> None:
        self.radius += 1
        layer = choices([False, True], k=8 * self.radius)
        self._squares_org.append(layer)
        self._squares.append(layer.copy())

    def print_kmoves(self, k: int) -> None:
        d = (0, 1)
        i = j = 0
        sq = self._squares

        for _ in range(k):
            r, t = self._translate_indices(i, j)

            if r > self.radius:
                self._expand()

            c = sq[r][t]
            sq[r][t] = not c

            # d0d1c -> sign
            # -------------
            # 100 -> 1
            # n00 -> 1
            # 010 -> -1
            # 0n0 -> -1
            sign = 2 * (abs(d[1]) == c) - 1
            d = sign * d[1], sign * d[0]
            i += d[0]
            j += d[1]

        print(f"Before:\n{self._str(org=True)}\n\nAfter:\n{self}")


class TestSolution(TestCase):
    def test(self) -> None:
        # Just look at the printed grids!
        a = Ant()
        a.print_kmoves(6)


if __name__ == "__main__":
    main()
