import operator
import re
from random import choices, randrange
from typing import Callable
from unittest import TestCase, main


def interpret_num_op_list(
    num_op_list: list[str],
    op_dict: dict[str, Callable[[float, float], float]],
) -> str:
    result = float(num_op_list[0])
    op_list = num_op_list[1::2]
    num_list = num_op_list[2::2]
    for op, num in zip(op_list, num_list):
        result = op_dict[op](result, float(num))
    return str(result)


def solve(s: str) -> float:
    addsub = re.compile(r"([\+\-])")
    muldiv = re.compile(r"([\*/])")
    addsub_dict = {"+": operator.add, "-": operator.sub}
    muldiv_dict = {"*": operator.mul, "/": operator.truediv}

    terms = re.split(addsub, s)
    terms[::2] = [
        interpret_num_op_list(re.split(muldiv, t), muldiv_dict) for t in terms[::2]
    ]
    result = interpret_num_op_list(terms, addsub_dict)
    return float(result)


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
