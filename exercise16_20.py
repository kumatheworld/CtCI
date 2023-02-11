from unittest import TestCase, main


def solve(n: int, d: list[str]) -> list[str]:
    phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    digits = [int(c) for c in str(n)]
    words = [w for w in d if len(w) == len(digits)]
    for i, dg in enumerate(digits):
        words = [w for w in words if w[i] in phone[dg]]
    return words


class TestSolution(TestCase):
    def test(self) -> None:
        with open("/usr/share/dict/words") as f:
            d = [w.rstrip() for w in f]

        # Just look at the printed lists!
        data = [8733, 27225, 843, 2633, 468378439]
        for n in data:
            print(n, solve(n, d))


if __name__ == "__main__":
    main()
