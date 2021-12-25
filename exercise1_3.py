from unittest import TestCase, main


def solve(s: str, k: int) -> str:
    return s.rstrip().replace(" ", "%20")


class TestSolution(TestCase):
    def test(self):
        pairs = [
            (("Mr John Smith    ", 13), "Mr%20John%20Smith"),
            (("kuma  the world      ", 15), "kuma%20%20the%20world"),
        ]
        for (s, k), t in pairs:
            self.assertEqual(solve(s, k), t)


if __name__ == "__main__":
    main()
