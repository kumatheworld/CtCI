from unittest import TestCase, main


def solve(p: str, v: str) -> bool:
    return True


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
