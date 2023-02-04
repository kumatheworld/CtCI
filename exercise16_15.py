from collections import Counter
from typing import Literal, TypeAlias
from unittest import TestCase, main

Color: TypeAlias = Literal["R", "Y", "G", "B"]
Slots: TypeAlias = tuple[Color, Color, Color, Color]
Hits: TypeAlias = Literal[0, 1, 2, 3]


def solve(g: Slots, s: Slots) -> tuple[Hits, Hits]:
    h = sum(1 for c, d in zip(g, s) if c == d)
    ph = sum((Counter(g) & Counter(s)).values()) - h
    return h, ph


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            ((tuple("GGRR"), tuple("RGBY")), (1, 1)),
            ((tuple("RGBY"), tuple("GGRR")), (1, 1)),
            ((tuple("BYGG"), tuple("GRYB")), (0, 3)),
            ((tuple("YBRB"), tuple("RYGB")), (1, 2)),
        ]
        for x, y in data:
            self.assertEqual(solve(*x), y)


if __name__ == "__main__":
    main()
