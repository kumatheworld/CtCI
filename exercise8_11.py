from collections import deque
from unittest import TestCase, main


def solve(n: int) -> int:
    return 0


class TestSolution(TestCase):
    @staticmethod
    def solve_dp(n: int) -> int:
        q01 = deque([1])
        q05 = deque([0] * 4 + [1])
        q10 = deque([0] * 9 + [1])
        q25 = deque([0] * 24 + [1])
        for _ in range(n):
            n01 = q01.popleft()
            n05 = n01 + q05.popleft()
            n10 = n05 + q10.popleft()
            n25 = n10 + q25.popleft()
            q01.append(n01)
            q05.append(n05)
            q10.append(n10)
            q25.append(n25)
        return q25[-1]

    def test(self) -> None:
        for i in range(1000):
            self.assertEqual(solve(i), self.solve_dp(i))


if __name__ == "__main__":
    main()
