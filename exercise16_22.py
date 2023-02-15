from random import choices


class Grid:
    def __init__(self) -> None:
        self.radius = 0
        self._squares = []

    def _expand(self) -> None:
        self.radius += 1
        self._squares.append(choices([False, True], k=8 * self.radius))
