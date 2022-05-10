from dataclasses import dataclass
from enum import IntEnum
from random import shuffle


class Suit(IntEnum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3


class Number(IntEnum):
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


@dataclass
class Card:
    suit: Suit
    number: Number

    def __repr__(self) -> str:
        return "SHDC"[self.suit] + " A23456789TJQK"[self.number]


class Deck:
    def __init__(self) -> None:
        self.cards = [Card(suit, number) for suit in Suit for number in Number]

    def __repr__(self) -> str:
        return repr(self.cards)

    def shuffle(self) -> None:
        shuffle(self.cards)
