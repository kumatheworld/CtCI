from random import choices


class Grid:
    def __init__(self) -> None:
        self.radius = 0
        self._squares = [choices([False, True], k=1)]

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
        self._squares.append(choices([False, True], k=8 * self.radius))
