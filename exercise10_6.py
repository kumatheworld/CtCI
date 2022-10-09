from collections import deque
from heapq import merge
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory, TemporaryFile
from unittest import TestCase, main


def solve(p: Path, split_lines: int = 1000) -> None:
    with TemporaryDirectory() as dirname:
        # Split files
        run(
            ["split", "-l", str(split_lines), str(p.resolve())], cwd=dirname, check=True
        )

        # Sort each file
        d1r = Path(dirname)
        for file in d1r.iterdir():
            run(["sort", "-o", file, file], cwd=dirname, check=True)

        # Merge sorted files
        q = deque(d1r.iterdir())
        while True:
            f0 = q.popleft()
            try:
                f1 = q.popleft()
            except IndexError:
                break
            with f0.open() as g0, f1.open() as g1, TemporaryFile() as f2:
                f2.writelines(s.encode() for s in merge(g0, g1))
                q.append(f2)
            f0.unlink()
            f1.unlink()


class TestSolution(TestCase):
    def test(self) -> None:
        pass


if __name__ == "__main__":
    main()
