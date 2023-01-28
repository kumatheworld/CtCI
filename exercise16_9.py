from unittest import TestCase, main

from numpy.random import randint


def multiply(x: int, y: int) -> int:
    # '<' and '-' are here. Is that ok?
    if y < 0:
        return -multiply(x, -y)

    z = 0
    for _ in range(y):
        z += x
    return z


def subtract(x: int, y: int) -> int:
    return x + multiply(y, -1)


def divide(x: int, y: int) -> int:
    if y == 0:
        raise ZeroDivisionError("integer division or modulo by zero")

    if y < 0:
        return divide(-x, -y)

    z = 0
    if x >= 0:
        w = y
        while x >= w:
            w += y
            z += 1
        return z
    else:
        w = x
        while w < 0:
            w += y
            z += 1
        return -z


class TestSolution(TestCase):
    def setUp(self) -> None:
        m = 1000
        n = 1000
        self.data = randint(-m, m, (n, 2))

    def test_multiply(self) -> None:
        for x, y in self.data:
            self.assertEqual(multiply(x, y), x * y)

    def test_subtract(self) -> None:
        for x, y in self.data:
            self.assertEqual(subtract(x, y), x - y)

    def test_divide_by_zero(self) -> None:
        for x, _ in self.data:
            with self.assertRaises(ZeroDivisionError):
                self.assertEqual(divide(x, 0))

    def test_divide_by_nonzero(self) -> None:
        for x, y in self.data:
            if y != 0:
                print(x, y)
                self.assertEqual(divide(x, y), x // y)


if __name__ == "__main__":
    main()
