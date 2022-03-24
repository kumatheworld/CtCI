from collections import deque
from unittest import TestCase, main

from common import CT


def solve(stack: deque[CT]) -> None:
    buf = deque[CT]()
    while stack:
        buf.append(stack.pop())
    while buf:
        x = buf.pop()
        count = 0
        while stack:
            if x < stack[-1]:
                break
            buf.append(stack.pop())
            count += 1
        stack.append(x)
        for _ in range(count):
            stack.append(buf.pop())


class TestSolution(TestCase):
    def test(self) -> None:
        data = ["", "o", "kk", "I am an unsorted stack"]
        for s in data:
            stack = deque(s)
            gt = deque(sorted(stack, reverse=True))
            solve(stack)
            self.assertEqual(stack, gt)


if __name__ == "__main__":
    main()
