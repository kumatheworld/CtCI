from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    name: str
    length: int
    page: int = 0

    def reset(self) -> None:
        self.page = 0

    def forward(self) -> None:
        if self.page < self.length:
            self.page += 1

    def backward(self) -> None:
        if self.page > 0:
            self.page -= 1

    def goto(self, page: int) -> None:
        if page < 0 or page >= self.length:
            raise IndexError("page out of range")
        self.page = page


@dataclass
class BookReader:
    books: list[Book]
    book: Optional[Book] = None

    def open(self, index: int) -> Book:
        self.book = self.books[index]
        return self.book

    def close(self) -> None:
        self.book = None
