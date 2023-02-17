from random import choices


class Grid:
    def __init__(self) -> None:
        self.radius = 0
        self._squares = [choices([False, True], k=1)]

    def _expand(self) -> None:
        self.radius += 1
        self._squares.append(choices([False, True], k=8 * self.radius))
