from unittest import TestCase, main

from exercise2 import LinkedList


def solve(x: LinkedList[int], y: LinkedList[int]) -> LinkedList[int]:
    # assume that x and y of the same length
    z = LinkedList()
    c = 0
    for a, b in zip(x, y):
        d = a + b + c
        c = d // 10
        z.append(d % 10)
    if c != 0:
        z.append(c)
    return z


class TestSolution(TestCase):
    def test(self) -> None:
        data = (("12345", "67890"), ("897438291", "263890129"))
        for sx, sy in data:
            x = LinkedList((int(d) for d in sx))
            y = LinkedList((int(d) for d in sy))
            z = solve(x, y)
            gt = LinkedList(int(d) for d in reversed(str(int(sx) + int(sy))))
            self.assertEqual(z, gt)


if __name__ == "__main__":
    main()
