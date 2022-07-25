class File:
    pass


class Directory(File):
    def __init__(self) -> None:
        self.files: dict[str, File] = {}
        self.dirs: dict[str, "Directory"] = {}
