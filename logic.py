import numpy as np


def squares(n: int):
    """Creates a list of the first n square numbers, beginning with 1."""
    lst = []
    for i in range(1, n + 1):
        lst.append(int(np.power(i, 2)))
    return lst