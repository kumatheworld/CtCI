from random import choices, getrandbits


class Grid:
    def __init__(self) -> None:
        self.radius = 0
        center = bool(getrandbits(1))
        self._squares_org = [[center]]
        self._squares = [[center]]

    def __str__(self) -> str:
        # Could be faster by bypassing __getitem__
        rng = range(-self.radius, self.radius + 1)
        return "\n".join("".join("xo"[self[i, j]] for j in rng) for i in rng)

    def __getitem__(self, ij: tuple[int, int]) -> bool:
        #  0 ~ 2r-1: ( n,  n) ... (-n+1, n)
        # 2r ~ 4r-1: (-n,  n) ... (-n, -n+1)
        # 4r ~ 6r-1: (-n, -n) ... (n-1, -n)
        # 6r ~ 8r-1: ( n, -n) ... ( n, n-1)
        i, j = ij
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
        return self._squares[r][t]

    def _expand(self) -> None:
        self.radius += 1
        layer = choices([False, True], k=8 * self.radius)
        self._squares_org.append(layer)
        self._squares.append(layer.copy())
