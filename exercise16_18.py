import re
from io import StringIO
from unittest import TestCase, main


def solve(p: str, v: str) -> bool:
    d = {}
    i = 0
    with StringIO() as f:
        for c in p:
            try:
                f.write(f"\\{d[c]}")
            except KeyError:
                i += 1
                d[c] = i
                f.write("(.*)")
        q = f.getvalue()
    r = re.compile(q)
    m = re.fullmatch(r, v)
    return bool(m)


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (("aabab", "catcatgocatgo"), True),
            (("a", "catcatgocatgo"), True),
            (("ab", "catcatgocatgo"), True),
            (("b", "catcatgocatgo"), True),
            (("", "catcatgocatgo"), False),
            (("aa", "catcatgocatgo"), False),
            (("aba", "catcatgocatgo"), True),
            (("bba", "catcatgocatgo"), True),
        ]
        for x, y in data:
            self.assertEqual(solve(*x), y)


if __name__ == "__main__":
    main()
