from abc import ABC, abstractmethod
from operator import itemgetter
from typing import Optional
from unittest import TestCase, main


class Strip:
    def __init__(self) -> None:
        self.days_until_positive: Optional[int] = None

    @property
    def positive(self) -> bool:
        return self.days_until_positive == 0


class Bottle:
    def __init__(self) -> None:
        self.poisonous = False


class Problem:
    def __init__(
        self,
        poisonous_bottle: int,
        days_to_see_result: int = 7,
        num_strips: int = 10,
        num_bottles: int = 1000,
    ) -> None:
        self.days_to_see_result = days_to_see_result
        self.strips = [Strip() for _ in range(num_strips)]
        self.bottles = [Bottle() for _ in range(num_bottles)]
        self.bottles[poisonous_bottle].poisonous = True
        self.testable = True
        self.day = 0

    def test(self, strip_id: int, bottle_ids: list[int]) -> None:
        if not self.testable:
            raise RuntimeError("you can only test once a day!")
        strip = self.strips[strip_id]
        if strip.days_until_positive is None:
            poisonous = any(self.bottles[i].poisonous for i in bottle_ids)
            if poisonous:
                strip.days_until_positive = self.days_to_see_result
        self.testable = False

    def end_day(self) -> None:
        for s in self.strips:
            if s.days_until_positive:
                s.days_until_positive -= 1
        self.testable = True
        self.day += 1


class Solution(ABC):
    def __init__(self, problem: Problem) -> None:
        super().__init__()
        self.problem = problem
        self.solution: Optional[int] = None

    @abstractmethod
    def step(self) -> None:
        pass


class Cheat(Solution):
    def step(self) -> None:
        for i, b in enumerate(self.problem.bottles):
            if b.poisonous:
                self.solution = i
                return
        raise RuntimeError("no poisonous bottle?")


class TestSolution(TestCase):
    def test(self) -> None:
        num_bottles = 1000
        days = []
        for i in range(num_bottles):
            p = Problem(i, num_bottles=num_bottles)
            s = Cheat(p)
            s.step()
            while s.solution is None:
                p.end_day()
                s.step()
            self.assertEqual(s.solution, i)
            days.append(p.day)
        im, dm = max(enumerate(days), key=itemgetter(1))
        print(
            f"Problem successfully solved!\n"
            f"Worst case: it took {dm} days "
            f"when the poisonous bottle id was {im} out of {num_bottles}."
        )


if __name__ == "__main__":
    main()
