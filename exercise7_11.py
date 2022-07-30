import os
from itertools import chain
from typing import Iterator, Optional


class File:
    pass


class Directory(File):
    def __init__(self, parent: Optional["Directory"] = None) -> None:
        self.parent = parent
        self.files: dict[str, File] = {}
        self.dirs: dict[str, "Directory"] = {}

    def touch(self, name: str) -> None:
        self.files[name] = File()

    def mkdir(self, name: str) -> None:
        if name in self.dirs:
            raise FileExistsError(
                f"Cannot create a file when that file already exists: '{name}'"
            )
        self.dirs[name] = Directory(parent=self)

    def ls(self) -> str:
        return " ".join(chain(self.files.keys(), (k + "/" for k in self.dirs.keys())))

    def _tree(self) -> Iterator[str]:
        for filename in self.files.keys():
            yield f"|-- {filename}"
        for dirname, d1r in self.dirs.items():
            yield f"|-- {dirname}"
            for line in d1r._tree():
                yield f"|   {line}"


class FileSystem:
    def __init__(self) -> None:
        self.root = self.cwd = Directory()
        self.pwd = os.path.sep
        self.owd: Optional[Directory] = None
