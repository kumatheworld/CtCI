from unittest import TestCase, main

from numpy.random import randint


def multiply(x: int, y: int) -> int:
    return 0


def subtract(x: int, y: int) -> int:
    return 0


def divide(x: int, y: int) -> int:
    return 0


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
