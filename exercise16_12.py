from collections.abc import Mapping
from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase, main
from xml.etree.ElementTree import Element, fromstring


def solve(t: Element, m: Mapping[str, int], end="\n") -> None:
    # Print tag
    print(m[t.tag], end=" ")

    # Where t has children or not
    # If it doesn't, print the text later
    b = bool(t)

    # Print attributes
    for k, v in t.attrib.items():
        print(m[k], v, end=" ")

    # Print END
    print(0, end=" ")

    # Print text if t doesn't have children
    if not b:
        print(t.text, end=" ")

    # Print children if it does
    for s in t:
        solve(s, m, end=" ")

    # Print END
    print(0, end=end)


class TestSolution(TestCase):
    def test(self) -> None:
        t = fromstring(
            """<family lastName="McDowell" state="CA">
            <person firstName="Gayle">Some Message</person>
            </family>"""
        )
        m = dict(family=1, person=2, firstName=3, lastName=4, state=5)
        s = "1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0\n"

        f = StringIO()
        with redirect_stdout(f):
            solve(t, m)
        self.assertEqual(f.getvalue(), s)


if __name__ == "__main__":
    main()
