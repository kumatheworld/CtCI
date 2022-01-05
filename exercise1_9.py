from unittest import TestCase, main


def is_substring(s: str, t: str) -> bool:
    return s.find(t) != -1


def solve(s: str, t: str) -> bool:
    return len(s) == len(t) and is_substring(s + s, t)


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = [("waterbottle", "erbottlewat"), ("python", "onpyth"), ("(@@)", "@)(@")]
        for s, t in data:
            self.assertTrue(solve(s, t))

    def test_neg(self) -> None:
        data = [("kuma", "mak"), ("mak", "kuma"), ("water", "teraw")]
        for s, t in data:
            self.assertFalse(solve(s, t))


if __name__ == "__main__":
    main()
