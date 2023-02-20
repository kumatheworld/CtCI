from collections import Counter
from random import randrange
from unittest import TestCase, main


def solve() -> int:
    x = 5 * randrange(5) + randrange(5)
    if x > 20:
        return solve()
    return x % 7


class TestSolution(TestCase):
    def test(self) -> None:
        # Just look at the printed counter!
        n = 700_000
        counter = Counter([solve() for _ in range(n)])
        print(counter)


if __name__ == "__main__":
    main()
