from random import choices


class Grid:
    def __init__(self) -> None:
        self.radius = 0
        self.squares = []

    def expand(self) -> None:
        self.radius += 1
        self.squares.append(choices([False, True], k=8 * self.radius))
