from unittest import TestCase, main


def solve(s: str, t: str, acc: int = 0) -> int:
    if len(s) == 0:
        return acc + len(t) <= 1
    if len(t) == 0:
        return acc + len(s) <= 1
    if s[0] == t[0]:
        return solve(s[1:], t[1:], acc)
    if acc == 1:
        return False
    return any(
        (
            solve(s[1:], t, acc + 1),
            solve(s, t[1:], acc + 1),
            solve(s[1:], t[1:], acc + 1),
        )
    )


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
