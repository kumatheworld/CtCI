from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class Comparable(Protocol):
    def __ge__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...

    def __le__(self, other: Any) -> bool:
        ...

    def __lt__(self, other: Any) -> bool:
        ...


CT = TypeVar("CT", bound=Comparable)
