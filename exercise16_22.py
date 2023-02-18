from random import choices, getrandbits


class Grid:
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
                t = i - r
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
