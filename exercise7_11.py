class File:
    pass


class Directory(File):
    def __init__(self) -> None:
        self.files: dict[str, File] = {}
        self.dirs: dict[str, "Directory"] = {}

    def touch(self, name: str) -> None:
        self.files[name] = File()

    def mkdir(self, name: str) -> None:
        if name in self.dirs:
            raise FileExistsError(
                f"Cannot create a file when that file already exists: '{name}'"
            )
        self.dirs[name] = Directory()
