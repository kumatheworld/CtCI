from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
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
        pass


class TestSolution(TestCase):
    def test(self) -> None:
        pass


if __name__ == "__main__":
    main()
