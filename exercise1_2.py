from unittest import TestCase, main


def solve(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


class TestSolution(TestCase):
    def test_pos(self):
        pairs = [("(@@)", "@)(@"), ("bear", "bare"), ("there", "three")]
        for s, t in pairs:
            self.assertTrue(solve(s, t))

    def test_neg(self):
        pairs = [(" ", "  "), ("treat", "tear"), ("which", "witch")]
        for s, t in pairs:
            self.assertFalse(solve(s, t))


if __name__ == "__main__":
    main()
