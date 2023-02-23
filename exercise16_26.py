from random import choices, randrange
from unittest import TestCase, main


def solve(s: str) -> float:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        iter = 1000
        m = 100
        n = 1000
        nums = range(m)
        ops = "+-*/"
        for _ in range(iter):
            k = randrange(n)
            num_list = choices(nums, k=k + 1)
            op_list = choices(ops, k=k)
            l = [str(num_list[-1])]
            for op, num in zip(op_list, num_list):
                l.append(op)
                l.append(str(num))
            s = "".join(l)
            try:
                y = eval(s)
            except ZeroDivisionError:
                with self.assertRaises(ZeroDivisionError):
                    solve(s)
            else:
                self.assertAlmostEqual(solve(s), y)


if __name__ == "__main__":
    main()
