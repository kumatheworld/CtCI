from typing import Iterator, Literal, TypeAlias
from unittest import TestCase, main

TowerID: TypeAlias = Literal[0, 1, 2]


class DiskSizeError(RuntimeError):
    pass


class TowersOfHanoi:
    def __init__(self, height: int) -> None:
        self.height = height
        self._towers: list[list[int]] = [list(range(height - 1, -1, -1)), [], []]

    def __str__(self) -> str:
        return "\n".join(
            f"{i}: {' '.join(str(disk) for disk in tower)}"
            for i, tower in enumerate(self._towers)
        )

    def move(self, src: TowerID, dst: TowerID) -> None:
        towers = self._towers
        ts = towers[src]
        disk = ts.pop()
        td = towers[dst]
        if td and td[-1] < disk:
            raise DiskSizeError(f"can't put disk {disk} on top of disk {td[-1]}")
        td.append(disk)

    def is_done(self) -> bool:
        t0, t1, t2 = self._towers
        return t0 == [] and t1 == [] and t2 == list(range(self.height - 1, -1, -1))


def solve(h: int) -> Iterator[tuple[TowerID, TowerID]]:
    if h == 0:
        return

    perm = [0, 2, 1]
    for src, dst in solve(h - 1):
        yield perm[src], perm[dst]

    yield 0, 2

    perm = [1, 0, 2]
    for src, dst in solve(h - 1):
        yield perm[src], perm[dst]


class TestSolution(TestCase):
    def test(self) -> None:
        for h in range(10):
            moves = solve(h)
            t = TowersOfHanoi(h)
            for m in moves:
                t.move(*m)
            self.assertTrue(t.is_done())


if __name__ == "__main__":
    main()
