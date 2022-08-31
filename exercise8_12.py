from itertools import permutations
from unittest import TestCase, main


def solve(n: int = 8) -> list[tuple[int, ...]]:
    return []


class TestSolution(TestCase):
    @staticmethod
    def is_valid(t: tuple[int, ...]) -> bool:
        l = len(t)
        return (
            sorted(t) == list(range(l))
            and len(set(i - j for i, j in enumerate(t)))
            == len(set(i + j for i, j in enumerate(t)))
            == l
        )

    def test(self) -> None:
        n = 8
        p = permutations(range(n))
        l = [t for t in p if self.is_valid(t)]
        print(sorted(solve(n)) == l)


if __name__ == "__main__":
    main()
