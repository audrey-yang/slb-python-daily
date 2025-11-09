"""
RandoMaps
Difficulty: Hard
What can be the output of the following snippet?

Options:
X. [2, 14, 9, 4, 2, 14, -1] for the inputs (10, 20, 7)
B. [10, 15, -1, 12, -1, -1] for the inputs (10, 25, 7)
C. [6, 2, -1, 18, 16, 9, 28] for the inputs (10, 33, 7)
D. [7, 15, 9, 2, 13, -1, 13] for the inputs (10, 19, 7)
"""

from random import randint


def myfunc(lower_limit, upper_limit, times=5) -> list:
    mean = (lower_limit + upper_limit) // 2
    a = map(lambda x: x if x < mean else -1,
            [randint(0, upper_limit) for _ in range(times)])

    return list(a)


"""
Considering each option:

A. [2, 14, 9, 4, 2, 14, -1] for the inputs (10, 20, 7)
    mean = 15
    This is possible as all values are less than the mean.

B. [10, 15, -1, 12, -1, -1] for the inputs (10, 25, 7)
    mean = 17
    This is not possible as there are only 6 values present.

C. [6, 2, -1, 18, 16, 9, 28] for the inputs (10, 33, 7)
    mean = 21
    This is not possible as 28 is greater than the mean.

D. [7, 15, 9, 2, 13, -1, 13] for the inputs (10, 19, 7)
    mean = 14
    This is not possible as 15 is greater than the mean.
"""

if __name__ == "__main__":
    print("Solution: A")
