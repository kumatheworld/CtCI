from itertools import permutations
from unittest import TestCase, main


def solve(n: int = 8) -> list[tuple[int, ...]]:
    lists = []

    def solve_(ok: list[list[int]], acc: list[int]) -> None:
        if not ok:
            lists.append(acc)
            return

        if not (ok_head := ok[0]):
            return

        for j in ok_head:
            ok_tail = ok[1:]
            for k, l in enumerate(ok_tail):
                ok_tail[k] = [i for i in l if i not in (j - k - 1, j, j + k + 1)]
            solve_(ok_tail, [*acc, j])

    solve_([list(range(n)) for _ in range(n)], [])

    return [tuple(l) for l in lists]


class TestSolution(TestCase):
    @staticmethod
    def is_valid(t: tuple[int, ...]) -> bool:
        l = len(t)
        return (
            sorted(t) == list(range(l))
            and len(set(i - j for i, j in enumerate(t)))
            == len(set(i + j for i, j in enumerate(t)))
            == l
        )

    def test(self) -> None:
        n = 8
        p = permutations(range(n))
        l = [t for t in p if self.is_valid(t)]
        print(sorted(solve(n)) == l)


if __name__ == "__main__":
    main()
