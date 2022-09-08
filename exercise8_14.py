from functools import cache
from itertools import chain
from random import choices
from unittest import TestCase, main


def solve(s: str, b: bool) -> int:
    return 0


class TestSolution(TestCase):
    @staticmethod
    @cache
    def solve_naive(s: str, b: bool) -> int:
        if len(s) == 1:
            return int(s) == b

        f = TestSolution.solve_naive
        count = 0
        for i, op in enumerate(s[1::2], 1):
            l = s[: 2 * i - 1]
            r = s[2 * i :]
            lt = f(l, True)
            lf = f(l, False)
            rt = f(r, True)
            rf = f(r, False)
            match op:
                case "&":
                    count += lt * rt if b else lf * rf + lf * rt + lt * rf
                case "|":
                    count += lf * rt + lt * rf + rt * lt if b else lf * rf
                case "^":
                    count += lf * rt + lt * rf if b else lf * rf + lt * rt
                case _:
                    raise ValueError("Operator must be in ('&', '|', '^')")

        return count

    def test(self) -> None:
        n = 50
        for i in range(1, n):
            bits = "01"
            ops = "&|^"
            rand_bits = choices(bits, k=i + 1)
            rand_ops = choices(ops, k=i)
            s = "".join("".join(chain.from_iterable(zip(rand_bits[:-1], rand_ops))))[
                :-1
            ]
            b = bool(rand_bits[-1])
            self.assertEqual(solve(s, b), self.solve_naive(s, b))


if __name__ == "__main__":
    main()
