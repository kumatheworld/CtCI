import numpy as np


def solve(a: list[int]) -> None:
    # Is it allowed to print one value multiple times?
    # If not, just sort in-place and run through the array
    dup = np.full(32000, False)
    for i in a:
        if dup[i]:
            print(i)
        else:
            dup[i] = True
