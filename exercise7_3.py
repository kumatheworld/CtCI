from collections import UserList
from dataclasses import dataclass


@dataclass
class Clip:
    name: str

    def play(self) -> None:
        print(f"Playing {self.name}...")


class JukeBox(UserList[Clip]):
    def play(self, n: int) -> None:
        self[n].play()
