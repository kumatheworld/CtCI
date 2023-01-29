from unittest import TestCase, main


def solve(k: int, shorter: int, longer: int) -> list[int]:
    diff = longer - shorter
    shortest = k * shorter
    return [shortest + i * diff for i in range(k + 1)]


class TestSolution(TestCase):
    def test(self) -> None:
        # Just look at the printed list!
        k = 5
        shorter = 3
        longer = 7
        print(solve(k, shorter, longer))


if __name__ == "__main__":
    main()
