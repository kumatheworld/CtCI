from functools import cache
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
        data = [(("1^0|0|1", False), 2), (("0&0&0&1^1|0", True), 10)]
        for (s, b), c in data:
            self.assertEqual(solve(s, b), c)


if __name__ == "__main__":
    main()
