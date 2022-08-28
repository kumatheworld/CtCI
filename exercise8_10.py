from random import randrange
from typing import Any
from unittest import TestCase, main

from numpy import full
from PIL import Image, ImageDraw, ImageGrab


def solve(im: Image.Image, xy: tuple[int, int], value: Any) -> None:
    color = im.getpixel(xy)
    w, h = im.size
    unseen = full((w + 1, h + 1), True)
    unseen[w] = False
    unseen[:, h] = False
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def solve_(x: int, y: int) -> None:
        unseen[x, y] = False
        im.putpixel((x, y), value)
        for dx, dy in directions:
            x_ = x + dx
            y_ = y + dy
            if unseen[x_, y_] and im.getpixel((x_, y_)) == color:
                solve_(x_, y_)

    x, y = xy
    solve_(x, y)


class TestSolution(TestCase):
    def test(self) -> None:
        w = 32
        h = 32
        it = 10
        im = ImageGrab.grab()
        im = im.resize((w, h))
        for _ in range(it):
            im0 = im.copy()
            im1 = im.copy()
            xy = (randrange(w), randrange(h))
            value = (randrange(256), randrange(256), randrange(256))
            solve(im0, xy, value)
            ImageDraw.floodfill(im1, xy, value)
            self.assertEqual(im0, im1)


if __name__ == "__main__":
    main()
