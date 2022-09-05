from collections.abc import Iterator
from itertools import chain, combinations
from random import randint
from typing import Any, NamedTuple
from unittest import TestCase, main

from common import time_limit


class Box(NamedTuple):
    width: int
    height: int
    depth: int

    def __lt__(self, other: Any) -> bool:
        return (
            isinstance(other, Box)
            and self.width < other.width
            and self.height < other.height
            and self.depth < other.depth
        )

    @classmethod
    def randint(cls, a: int = 1, b: int = 256) -> "Box":
        return cls(*(randint(a, b) for _ in range(3)))


def solve(stack: list[Box]) -> int:
    boxes = [Box(0, 0, 0), *sorted(stack, key=tuple)]

    highests = [0]
    for box in boxes[1:]:
        h = box.height
        h_max = max(h + k for i, k in enumerate(highests) if boxes[i] < box)
        highests.append(h_max)

    return max(highests)


class TestSolution(TestCase):
    @staticmethod
    def generate_all_heights(stack: list[Box]) -> Iterator[int]:
        powerset = chain.from_iterable(
            combinations(stack, i) for i in range(len(stack) + 1)
        )
        for boxes in powerset:
            s = sorted(boxes)
            if all(b < c for b, c in zip(s[:-1], s[1:])):
                yield sum(box.height for box in boxes)

    def test(self) -> None:
        n = 10
        it = 100
        for _ in range(it):
            stack = [Box.randint() for _ in range(n)]
            heights = self.generate_all_heights(stack)
            self.assertEqual(solve(stack), max(heights))

    def test_speed(self) -> None:
        n = 1000
        t = 10
        stack = [Box.randint() for _ in range(n)]
        with time_limit(t):
            solve(stack)


if __name__ == "__main__":
    main()
