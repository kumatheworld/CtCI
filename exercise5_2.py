from unittest import TestCase, main


def solve(x: float) -> str:
    y = x * (1 << 32)
    if not y.is_integer():
        return "ERROR"
    a = f"{int(y):b}"
    b = "0" * (32 - len(a)) + a
    c = "." + b[: b.rfind("1") + 1]
    return c


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0.1, "ERROR"),
            (0.3125, ".0101"),
            (0.5, ".1"),
            (0.60823209374211728573, ".10011011101101010001100100110111"),
            (0.72, "ERROR"),
            (0.75, ".11"),
        ]
        for x, s in data:
            self.assertEqual(solve(x), s)


if __name__ == "__main__":
    main()
