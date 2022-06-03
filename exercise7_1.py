from abc import ABC, abstractmethod
from collections import UserList
from dataclasses import dataclass
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
            total += min((r := c.rank), 10)
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


class StandAlways(Player):
    def play(self) -> bool:
        return False


class DrawIfSafe(Player):
    def play(self) -> bool:
        score_low = sum(min(c.rank, 10) for c in self.hand)
        if score_low <= 11:
            return True
        return False


class DrawIfLEDealerPlusX(Player):
    def __init__(self, x: int = 10) -> None:
        super().__init__()
        self.x = x

    def play(self) -> bool:
        if 0 < self.hand.score <= min(self.dealer_card.rank, 10) + self.x:
            return True
        return False


@dataclass
class BlackJack:
    player: Player

    def play(self) -> int:
        """1 if player wins, 0 if draw, -1 if dealer wins"""
        deck = Deck()
        deck.shuffle()
        dealer = Hand([deck.pop(), deck.pop()])
        player = self.player
        player.init(dealer[0], (deck.pop(), deck.pop()))
        while player.play():
            player.hand.append(deck.pop())
        if (ps := player.hand.score) == 0:
            return -1
        while 0 < dealer.score < 17:
            dealer.append(deck.pop())
        ds = dealer.score
        if ps > ds:
            return 1
        if ps == ds:
            return 0
        return -1
