from unittest import TestCase, main


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def solve(x: int) -> int:
    s, b = bin(x).split("0b")
    if len(b) % 2:
        b = "0" + b
    c = "".join(y[::-1] for y in chunks(b, 2))
    d = int(c, 2)
    return -d if s else d


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0b0, 0b0),
            (0b1, 0b10),
            (-0b10, -0b1),
            (0b101001, 0b10110),
            (-0b101100111010001, -0b1010011011100010),
        ]
        for x, y in data:
            self.assertEqual(solve(x), y)
        for x in range(-10000, 10000):
            self.assertEqual(solve(solve(x)), x)


if __name__ == "__main__":
    main()
