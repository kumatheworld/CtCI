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
        self.testcase = randint(-m, m, (n, 2))

    def test_multiply(self) -> None:
        for x, y in self.testcase:
            self.assertEqual(multiply(x, y), x * y)

    def test_subtract(self) -> None:
        for x, y in self.testcase:
            self.assertEqual(subtract(x, y), x - y)

    def test_divide(self) -> None:
        for x, y in self.testcase:
            self.assertEqual(divide(x, y), x / y)


if __name__ == "__main__":
    main()
