from contextlib import suppress
from random import sample
from unittest import TestCase, main


def solve(l: list[int]) -> int:
    # Technically this takes O(log(n)) space to store the number len(l)
    if not l:
        return 0

    digit = 0
    while (n := len(l)) > 1:
        num_ones = sum((x >> digit) & 1 for x in l)
        if num_ones == 0:
            last = min(l)
            break
        majority = 2 * num_ones >= n
        with suppress(IndexError):
            i = 0
            while True:
                if (l[i] >> digit) & 1 == majority:
                    del l[i]
                else:
                    i += 1
        digit += 1
    else:
        last = l[0]

    return last ^ (1 << digit)


class TestSolution(TestCase):
    def test(self) -> None:
        n = 1000
        for i in range(1, n):
            l = sample(range(i), i)
            self.assertEqual(solve(l[:-1]), l[-1])


if __name__ == "__main__":
    main()
