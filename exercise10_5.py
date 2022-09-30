from collections import defaultdict
from random import randrange, sample
from typing import Sequence


class RandDivStr(Sequence[str]):
    def __init__(self, length: int, density: float = 0.1) -> None:
        self.length = length
        l3n = int(length * density)
        keys = sorted(sample(range(length), l3n))
        values_int = sorted(randrange(l3n) for _ in range(l3n))
        values = (str(i) for i in values_int)
        self.dict = defaultdict(str, zip(keys, values))

    def __str__(self) -> str:
        return str([self[i] for i in range(len(self))])

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, idx) -> str:
        return self.dict[idx]

    def index(self, value: str) -> int:
        for k, v in self.dict.items():
            print(k, v)
            if v == value:
                return k
        raise ValueError(f"{value} is not in list")
