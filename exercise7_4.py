from collections import UserList
from random import choice
from typing import NamedTuple, Optional


class Car:
    def __init__(self) -> None:
        self.place: Optional[Place] = None

    def park(self, pl: "ParkingLot", i: int) -> None:
        if self.place:
            raise RuntimeError("car already parked somewhere")
        if pl[i]:
            raise RuntimeError("another car parked here")
        pl[i] = self
        self.place = Place(pl, i)

    def park_nearest(self, pl: "ParkingLot") -> None:
        for i, j in enumerate(pl):
            if j is None:
                self.park(pl, i)
                return
        raise MemoryError("parking lot already full")

    def park_random(self, pl: "ParkingLot") -> None:
        vacant = [i for i, j in enumerate(pl) if j is None]
        if not vacant:
            raise MemoryError("parking lot already full")
        i = choice(vacant)
        self.park(pl, i)

    def go(self) -> None:
        place = self.place
        if place is None:
            raise RuntimeError()
        place.parking_lot[place.location] = None
        self.place = None


class ParkingLot(UserList[Optional[Car]]):
    def __init__(self, capacity: int) -> None:
        self.data = [None] * capacity


class Place(NamedTuple):
    parking_lot: ParkingLot
    location: int
