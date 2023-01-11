from unittest import TestCase, main


def solve(n: int) -> str:
    if n == 0:
        return "Zero"

    one_to_nineteen = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    twenty_to_Ninety = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    thousand_plus = ["Thousand", "Million", "Billion", "Trillion"]

    l = []
    i = 0
    while True:
        n, abc = divmod(n, 1000)
        a, bc = divmod(abc, 100)
        if bc:
            if bc < 20:
                l.append(one_to_nineteen[bc])
            else:
                b, c = divmod(bc, 10)
                if c:
                    l.append(one_to_nineteen[c])
                l.append(twenty_to_Ninety[b])
        if a:
            l.append("Hundred")
            l.append(one_to_nineteen[a])
        if n:
            l.append(thousand_plus[i] + ",")
            i += 1
        else:
            break

    return " ".join(reversed(l))


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            (0, "Zero"),
            (12, "Twelve"),
            (43, "Forty Three"),
            (56, "Fifty Six"),
            (789, "Seven Hundred Eighty Nine"),
            (1234, "One Thousand, Two Hundred Thirty Four"),
        ]
        for n, s in data:
            self.assertEqual(solve(n), s)


if __name__ == "__main__":
    main()
