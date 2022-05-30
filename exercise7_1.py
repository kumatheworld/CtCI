from abc import ABC, abstractmethod
from collections import UserList
from enum import IntEnum
from random import shuffle
from typing import NamedTuple


class Suit(IntEnum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3

    def __str__(self) -> str:
        return "SHDC"[self]


class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self) -> str:
        return " A23456789TJQK"[self]


class Card(NamedTuple):
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return str(self.suit) + str(self.rank)


class Cards(UserList[Card]):
    def __str__(self) -> str:
        return " ".join(str(c) for c in self)


class Deck(Cards):
    def __init__(self) -> None:
        self.data = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self) -> None:
        shuffle(self)


class Hand(Cards):
    @property
    def score(self) -> int:
        total = 0
        aces = 0
        for c in self:
            r = c.rank
            total += min(r, 10)
            if r == 1:
                aces += 1
            if total > 21:
                return 0
        for _ in range(aces):
            total_ = total + 10
            if total_ > 21:
                break
            total = total_
        return total


class Player(ABC):
    def init(self, dealer_card: Card, player_cards: tuple[Card, Card]) -> None:
        self.dealer_card = dealer_card
        self.hand = Hand(player_cards)

    @abstractmethod
    def play(self) -> bool:
        """True = hit, False = stand"""
        pass
