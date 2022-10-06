from pathlib import Path
from subprocess import run
from unittest import TestCase, main


def solve(p: Path) -> None:
    # Split files
    run(["split", str(p)])

    # Sort each file
    for file in ...:
        run(["sort", "-o", file, file])

    # Merge sorted files
    pass


class TestSolution(TestCase):
    def test(self) -> None:
        pass


if __name__ == "__main__":
    main()
