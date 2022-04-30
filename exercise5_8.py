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


def print_screen(screen: bytearray, width: int):
    w = width // 8
    for i, b in enumerate(screen, 1):
        print(f"{b:08b}", end=" ")
        if i % w == 0:
            print()


class TestSolution(TestCase):
    def test(self) -> None:
        # Change values to see how solve() works
        screen = bytearray([123, 45, 67, 89])
        width = 16
        x1 = 3
        x2 = 8
        y = 1
        print_screen(screen, width)
        solve(screen, width, x1, x2, y)
        print_screen(screen, width)


if __name__ == "__main__":
    main()
