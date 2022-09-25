class Listy(list[int]):
    def __getitem__(self, idx: int) -> int:
        if idx < 0:
            raise IndexError(f"negative index {idx} is not allowed")
        try:
            return super().__getitem__(idx)
        except IndexError:
            return -1

    def __repr__(self) -> str:
        return "Listy"

    def __len__(self) -> int:
        raise NotImplementedError
