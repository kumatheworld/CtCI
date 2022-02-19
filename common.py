from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar

T = TypeVar("T")


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)
