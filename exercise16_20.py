from unittest import TestCase, main


def solve(n: int, d: list[str]) -> list[str]:
    return []


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
