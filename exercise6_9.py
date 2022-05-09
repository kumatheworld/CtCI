def main() -> None:
    n = 100
    l = [False] * n
    for i in range(n):
        for j in range(i, n, i + 1):
            l[j] = not l[j]
    print(sum(l))


if __name__ == "__main__":
    main()
