import os
from collections.abc import Iterator
from itertools import chain
from typing import Optional


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
        return " ".join(chain(self.files, (k + "/" for k in self.dirs)))

    def _tree(self) -> Iterator[str]:
        for filename in self.files:
            yield f"|-- {filename}"
        for dirname, d1r in self.dirs.items():
            yield f"|-- {dirname}"
            for line in d1r._tree():
                yield f"|   {line}"


class FileSystem:
    def __init__(self) -> None:
        self.root = self.cwd = Directory()
        self.owd: Optional[Directory] = None
        self.dirnames: list[str] = []

    @property
    def pwd(self) -> str:
        return os.path.sep + os.path.sep.join(self.dirnames)

    def __str__(self) -> str:
        return self.pwd + "\n" + "\n".join(self.cwd._tree())

    def cd(self, path: str) -> None:
        if path == "-":
            if self.owd:
                self.cwd, self.owd = self.owd, self.owd
                return
            else:
                raise ValueError("Old working directory not set")

        norm_path = os.path.normpath(path)
        if norm_path == ".":
            self.owd = self.cwd
            return

        dirnames = norm_path.split(os.path.sep)
        self_dirnames = self.dirnames.copy()
        if os.path.isabs(norm_path):
            d1r = self.root
            del dirnames[0]
        else:
            d1r = self.cwd

        try:
            for name in dirnames:
                if name == "..":
                    if (parent := d1r.parent) is not None:
                        d1r = parent
                        self_dirnames.pop()
                else:
                    d1r = d1r.dirs[name]
                    self_dirnames.append(name)
        except KeyError:
            raise FileNotFoundError(
                f"The system cannot find the path specified: '{path}'"
            ) from None

        self.owd = self.cwd
        self.cwd = d1r
        self.dirnames = self_dirnames
