from typing import Literal, TypeAlias
from unittest import TestCase, main

Color: TypeAlias = Literal["R", "Y", "G", "B"]
Slots: TypeAlias = tuple[Color, Color, Color, Color]
Hits: TypeAlias = Literal[0, 1, 2, 3]


def solve(g: Slots, s2: Slots) -> tuple[Hits, Hits]:
    return 0, 0


class TestSolution(TestCase):
    def test(self) -> None:
        pass


if __name__ == "__main__":
    main()
