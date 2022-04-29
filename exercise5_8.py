from unittest import TestCase, main


def solve(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    o = (width // 8) * y
    if x2 < x1:
        x1, x2 = x2, x1
    q1 = x1 // 8
    r1 = x1 % 8
    m1 = (1 << (8 - r1)) - 1
    q2 = x2 // 8
    r2 = x2 % 8 + 1
    m2 = ((1 << r2) - 1) << (8 - r2)
    s = o + q1
    if q1 == q2:
        screen[s] |= m1 & m2
    else:
        t = o + q2
        screen[s] |= m1
        screen[s + 1 : t] = [255] * (t - s - 1)
        screen[t] |= m2


class TestSolution(TestCase):
    def test(self) -> None:
        pass


if __name__ == "__main__":
    main()
