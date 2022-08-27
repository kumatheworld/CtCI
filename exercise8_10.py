from random import randrange
from typing import Any
from unittest import TestCase, main

from PIL import Image, ImageDraw, ImageGrab


def solve(im: Image.Image, xy: tuple[int, int], value: Any) -> None:
    return


class TestSolution(TestCase):
    def test(self) -> None:
        w = 100
        h = 100
        it = 10
        im = ImageGrab.grab()
        im = im.resize((w, h))
        for _ in range(it):
            im0 = im.copy()
            im1 = im.copy()
            xy = (randrange(w), randrange(h))
            value = (randrange(256), randrange(256), randrange(256))
            solve(im1, xy, value)
            ImageDraw.floodfill(im1, xy, value)
            self.assertEqual(im0, im1)


if __name__ == "__main__":
    main()
