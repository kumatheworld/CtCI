from random import sample
from unittest import TestCase, main


def solve(names: dict[str, int], synonyms: list[tuple[str, str]]) -> dict[str, int]:
    return {}


class TestSolution(TestCase):
    def test(self) -> None:
        names = {"John": 15, "Jon": 12, "Chris": 13, "Kris": 4, "Christopher": 19}
        synonyms = [
            ("John", "Jon"),
            ("John", "Johnny"),
            ("Chris", "Kris"),
            ("Chris", "Christopher"),
        ]
        ans_set = {
            frozenset(["John", "Jon", "Johnny"]): 27,
            frozenset(["Chris", "Kris", "Christopher"]): 36,
        }
        for _ in range(100):
            names = dict(sample(list(names.items()), len(names)))
            synonyms = sample([tuple(sample(p, 2)) for p in synonyms], len(synonyms))
            pred = solve(names, synonyms)
            self.assertEqual(len(pred), len(ans_set))
            ans = {}
            for np in pred:
                for na, fp in ans_set.items():
                    if np in na:
                        ans[np] = fp
            self.assertEqual(pred, ans)


if __name__ == "__main__":
    main()
