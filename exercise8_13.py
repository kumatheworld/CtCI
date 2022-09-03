from random import randint
from typing import Any, NamedTuple


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
