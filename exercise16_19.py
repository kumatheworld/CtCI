from unittest import TestCase, main

import numpy as np


def solve(p: np.ndarray) -> list[int]:
    return []


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (
                np.array(
                    [
                        [0, 2, 1, 0],
                        [0, 1, 0, 1],
                        [1, 1, 0, 1],
                        [0, 1, 0, 1],
                    ]
                ),
                [2, 4, 1],
            ),
        ]
        for x, y in data:
            self.assertEqual(sorted(solve(x)), sorted(y))


if __name__ == "__main__":
    main()
