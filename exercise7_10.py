from dataclasses import dataclass
from enum import IntEnum


class ExplosiveNumber(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    MINE = 9


@dataclass
class Square:
    number: ExplosiveNumber = ExplosiveNumber.ZERO
    discovered: bool = False

    def __str__(self) -> str:
        return str(int(self.number)) if self.discovered else " "
