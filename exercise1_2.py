from unittest import TestCase, main


def solve(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = [("(@@)", "@)(@"), ("bear", "bare"), ("there", "three")]
        for s, t in data:
            self.assertTrue(solve(s, t))

    def test_neg(self) -> None:
        data = [(" ", "  "), ("treat", "tear"), ("which", "witch")]
        for s, t in data:
            self.assertFalse(solve(s, t))


if __name__ == "__main__":
    main()
