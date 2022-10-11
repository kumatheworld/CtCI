from collections.abc import Iterator
from heapq import merge
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from unittest import TestCase, main


def generate_lines_from_file(p: Path) -> Iterator[str]:
    with p.open() as f:
        yield from f


def solve(p: Path, lines: int = 1000) -> Iterator[str]:
    with TemporaryDirectory() as dirname:
        # Split files
        run(["split", "-l", str(lines), str(p.resolve())], cwd=dirname, check=True)

        # Sort each file
        d1r = Path(dirname)
        for file in d1r.iterdir():
            run(["sort", "-o", file, file], cwd=dirname, check=True)

        # Merge sorted files
        yield from merge(*(generate_lines_from_file(ph) for ph in d1r.iterdir()))


class TestSolution(TestCase):
    def test(self) -> None:
        solve(Path(__file__), 3)


if __name__ == "__main__":
    main()
