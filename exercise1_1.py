from unittest import TestCase, main


def solve(s: str) -> bool:
    return len(set(s)) == len(s)


class TestSolution(TestCase):
    def test_pos(self) -> None:
        ss = ["kuma", "the", "world", "so", "much", "fun"]
        for s in ss:
            self.assertTrue(solve(s))

    def test_neg(self) -> None:
        ss = ["hello", "kuma the world", "amazing"]
        for s in ss:
            self.assertFalse(solve(s))


if __name__ == "__main__":
    main()
