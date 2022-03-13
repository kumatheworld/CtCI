from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar

T = TypeVar("T")


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __ge__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __le__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)
