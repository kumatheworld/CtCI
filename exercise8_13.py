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
