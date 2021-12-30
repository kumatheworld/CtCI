from unittest import TestCase, main


def solve(s: str) -> bool:
    return len(set(s)) == len(s)


class TestSolution(TestCase):
    def test_pos(self) -> None:
        data = ["kuma", "the", "world", "so", "much", "fun"]
        for s in data:
            self.assertTrue(solve(s))

    def test_neg(self) -> None:
        data = ["hello", "kuma the world", "amazing"]
        for s in data:
            self.assertFalse(solve(s))


if __name__ == "__main__":
    main()
