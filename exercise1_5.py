from unittest import TestCase, main


def solve(s: str, t: str) -> int:
    if len(s) == 0:
        return len(t) <= 1
    if len(t) == 0:
        return len(s) <= 1
    if s[0] == t[0]:
        return solve(s[1:], t[1:])
    return any((s[1:] == t, s == t[1:], s[1:] == t[1:]))


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = [("pale", "ple"), ("pales", "pale"), ("pale", "bale")]
        for s, t in data:
            self.assertTrue(solve(s, t))

    def test_neg(self) -> None:
        data = [("pale", "bake"), ("crack", "quack"), ("code", "kobe")]
        for s, t in data:
            self.assertFalse(solve(s, t))


if __name__ == "__main__":
    main()
