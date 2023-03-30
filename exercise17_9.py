from itertools import product
from unittest import TestCase, main


def solve(n: int) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        m = 100
        rng = range(m)
        nums = sorted(
            3**n3 * 5**n5 * 7**n7 for n3, n5, n7 in product(rng, rng, rng)
        )
        for n in range(nums.index(3 ** (m - 1))):
            self.assertEqual(solve(n), nums[n])


if __name__ == "__main__":
    main()
