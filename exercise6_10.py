from abc import ABC, abstractmethod
from unittest import TestCase, main


class Strip:
    def __init__(self) -> None:
        self.positive = False


class Bottle:
    def __init__(self) -> None:
        self.poisonous = False


class Problem:
    def __init__(self, num_strips: int = 10, num_bottles: int = 1000) -> None:
        self.strips = [Strip() for _ in range(num_strips)]
        self.bottles = [Bottle() for _ in range(num_bottles)]


class Solution(ABC):
    @abstractmethod
    def solve(self) -> int:
        pass


class TestSolution(TestCase):
    def test(self) -> None:
        pass


if __name__ == "__main__":
    main()
