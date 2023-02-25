from random import choices, randrange
from unittest import TestCase, main


def solve(l: list[int]) -> int:
    def solve_(offset: int, length: int) -> tuple[int, int, int, int]:
        if length < 2:
            s_ = l[offset] if length else 0
            l_ = m_ = r_ = max(0, s_)
            return s_, l_, m_, r_
        h = length // 2
        sl, ll, ml, rl = solve_(offset, h)
        sr, lr, mr, rr = solve_(offset + h, length - h)
        s_ = sl + sr
        l_ = max(ll, sl + lr)
        r_ = max(rl + sr, rr)
        m_ = max(l_, ml, rl + lr, mr, r_)
        return s_, l_, m_, r_

    _, _, m, _ = solve_(0, len(l))
    return m


class TestSolution(TestCase):
    def test(self) -> None:
        iter = 1000
        m = 100
        p = range(-m, m)
        for _ in range(iter):
            k = randrange(m)
            l = choices(p, k=k)
            s = 0
            for i in range(k):
                for j in range(i + 1, k + 1):
                    s = max(s, sum(l[i:j]))
            self.assertEqual(solve(l), s)


if __name__ == "__main__":
    main()
    main()
