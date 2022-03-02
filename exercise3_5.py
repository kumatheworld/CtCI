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
            y = stack[-1]
            if x < y:
                break
            buf.append(stack.pop())
            count += 1
        stack.append(x)
        for _ in range(count):
            stack.append(buf.pop())


class TestSolution(TestCase):
    def test(self) -> None:
        for data in ("", "o", "kk", "I am an unsorted stack"):
            stack = deque(data)
            gt = deque(sorted(stack, reverse=True))
            solve(stack)
            self.assertEqual(stack, gt)


if __name__ == "__main__":
    main()