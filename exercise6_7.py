from random import random


def bear(p: int) -> int:
    n = 0
    while random() < p:
        n += 1
    return n


def main() -> None:
    p = 0.5
    n = 1000000
    r = sum(bear(p) for _ in range(n)) / n
    print(r)


if __name__ == "__main__":
    main()
