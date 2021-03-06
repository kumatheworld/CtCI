from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from itertools import product
from random import choice
from typing import Literal, Optional, TypeAlias

Coordinate: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
Point: TypeAlias = tuple[Coordinate, Coordinate]


class Color(Enum):
    BLACK = False
    WHITE = True

    def __str__(self) -> str:
        return "xo"[self.value]

    def opposite(self) -> "Color":
        return Color(not self.value)


@dataclass
class Square:
    state: Optional[Color] = None
    flippable_points: set[Point] = field(default_factory=set)

    def __str__(self) -> str:
        return "." if self.state is None else str(self.state)


class Direction(Enum):
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    SW = (-1, 1)
    W = (-1, 0)
    NW = (-1, -1)
    N = (0, -1)
    NE = (1, -1)


class Othello:
    def __init__(
        self,
        player_black: "Player",
        player_white: "Player",
    ) -> None:
        board = tuple(tuple(Square() for _ in range(8)) for _ in range(8))
        board[3][3].state = Color.WHITE
        board[3][4].state = Color.BLACK
        board[4][3].state = Color.BLACK
        board[4][4].state = Color.WHITE
        self.board = board
        self.player_black = player_black
        self.player_white = player_white

    def __str__(self) -> str:
        return "\n".join("".join(str(square) for square in row) for row in self.board)

    def play(self) -> None:
        board = self.board
        color = Color.BLACK
        placeable_points = [
            (x, y)
            for x, y in product(range(8), range(8))
            if x < 3 or 4 < x or y < 3 or 4 < y
        ]
        player_on = self.player_black
        player_off = self.player_white
        stuck = False

        while placeable_points:
            # Compute flippable points
            for x, y in placeable_points:
                flippable_points: set[Point] = set()
                for d in Direction:
                    dx, dy = d.value
                    xx, yy = x + dx, y + dy
                    fps: set[Point] = set()
                    while xx in range(8) and yy in range(8):
                        match board[xx][yy].state:
                            case None:
                                break
                            case c if c is color:
                                flippable_points |= fps
                                break
                            case _:
                                fps.add((xx, yy))
                        xx += dx
                        yy += dy
                board[x][y].flippable_points = flippable_points

            if any(
                board[x][y].flippable_points for x, y in product(range(8), range(8))
            ):
                # Player plays their turn
                x, y = player_on.play(othello)
                (square := board[x][y]).state = color
                for xx, yy in square.flippable_points:
                    board[xx][yy].state = color
                square.flippable_points = set()
                placeable_points.remove((x, y))
                stuck = False
            else:
                if stuck:
                    break
                stuck = True

            # End turn
            player_on, player_off = player_off, player_on
            color = color.opposite()


class Player(ABC):
    @abstractmethod
    def play(self, othello: Othello) -> Point:
        pass


class RandomPlayer(Player):
    def play(self, othello: Othello) -> Point:
        return choice(
            [
                (x, y)
                for x, y in product(range(8), range(8))
                if othello.board[x][y].flippable_points
            ]
        )


class RandomMaxPlayer(Player):
    def play(self, othello: Othello) -> Point:
        num_flippable_points = [
            ((x, y), len(othello.board[x][y].flippable_points))
            for x, y in product(range(8), range(8))
        ]
        num_flippable_points_max = max(n for _, n in num_flippable_points)
        return choice(
            [
                (x, y)
                for (x, y), n in num_flippable_points
                if n == num_flippable_points_max
            ]
        )


class RandomCornerPlayer(Player):
    def play(self, othello: Othello) -> Point:
        flippable_points_with_dist = [
            ((x, y), abs(2 * x - 7) + abs(2 * y - 7))
            for x, y in product(range(8), range(8))
            if othello.board[x][y].flippable_points
        ]
        dist_max = max(d for _, d in flippable_points_with_dist)
        return choice(
            [(x, y) for (x, y), d in flippable_points_with_dist if d == dist_max]
        )


if __name__ == "__main__":
    player_black = RandomPlayer()
    player_white = RandomCornerPlayer()
    othello = Othello(player_black, player_white)

    othello.play()
    result = dict(Counter([str(s) for r in othello.board for s in r]))
    print(othello)
    print(result)
