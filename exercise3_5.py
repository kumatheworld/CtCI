from collections import deque
from unittest import TestCase, main

from common import CT


def solve(stack: deque[CT]) -> None:
    if not stack:
        return

    buf = deque[CT]()
    len_stack = 0
    while stack:
        buf.append(stack.pop())
        len_stack += 1
    for _ in range(len_stack):
        stack.append(buf.pop())

    num_unsorted = len_stack
    while num_unsorted:
        max_elem = stack.pop()
        buf.append(max_elem)
        len_buf = 1
        max_count = 1
        while len_buf < num_unsorted:
            elem = stack.pop()
            buf.append(elem)
            len_buf += 1
            if max_elem == elem:
                max_count += 1
            elif max_elem < elem:
                max_elem = elem
                max_count = 1
        for _ in range(max_count):
            stack.append(max_elem)
        while buf:
            elem = buf.pop()
            if elem != max_elem:
                stack.append(elem)
        num_unsorted -= max_count


class TestSolution(TestCase):
    def test(self) -> None:
        for data in ("", "o", "kk", "I am an unsorted stack"):
            stack = deque(data)
            gt = deque(sorted(stack, reverse=True))
            solve(stack)
            self.assertEqual(stack, gt)


if __name__ == "__main__":
    main()
