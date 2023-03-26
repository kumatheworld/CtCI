from itertools import accumulate
from unittest import TestCase, main


def solve(n: int) -> int:
    # Slower!
    num_2s_above = accumulate(int(c == "2") for c in "0" + str(n)[:-1])
    count = 0
    for i, (d_str, n2b) in enumerate(reversed(list(zip(str(n), num_2s_above)))):
        d = int(d_str)
        tti = 10**i
        count += n2b * d * tti + i * d * tti // 10 + (d > 2) * tti + (d == 2)
    return count


class TestSolution(TestCase):
    def test(self) -> None:
        m = 1_000_000
        count = 0
        for n in range(m):
            count += str(n).count("2")
            self.assertEqual(solve(n), count)


if __name__ == "__main__":
    main()
