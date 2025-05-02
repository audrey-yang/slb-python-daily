"""
Inverse Squares

Difficulty: Easy
Find the sum of the following mathematical series up to $n$ terms, using recursion.
$1/1^2 + 1/2^2 + . . . + 1/n^2 = sum_k^n 1/k^2$
Note - Round off the result to 5 decimal places.

Examples:

Test Case 1:
Input: 3
Output: 1.36111
Explanation: 1 + 1/4 + 1/9 = 1.36111

Test Case 2:
Input: 5
Output: 1.46361
Explanation: 1 + 1/4 + 1/9 + 1/16 + 1/25 = 1.46361
"""


def inverse_squares(n: int) -> float:
    assert n > 0
    return round((inverse_squares(n - 1) if n > 1 else 0) + (1 / (n ** 2)), 5)


def test_1():
    assert inverse_squares(3) == 1.36111


def test_2():
    assert inverse_squares(5) == 1.46361


def test_3():
    assert inverse_squares(1) == 1


def test_4():
    error_was_thrown = False
    try:
        inverse_squares(0)
    except AssertionError:
        error_was_thrown = True
    assert error_was_thrown is True


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    print("All tests passed.")
