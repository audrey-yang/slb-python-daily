"""
Minimum Greater

Given a list of sorted integers, find in it the smallest number bigger than a given number 'a'.

If all numbers in the given list are smaller than 'a', return -1.

Examples:

Test Case 1:
Input: [3,7,12,20,21,25], 5
Output: 7
Explanation: There are many numbers in the list bigger than 5, but the smallest of them is 7.

Test Case 2:
Input: [10,20,30], 0
Output: 10
Explanation: The smallest number in the list bigger than 0 is 10.
"""


def minimum_greater(lst: list[int], a: int) -> int:
    """
    Finds the smallest number in the input list that is greater than a

    Args:
        lst (list): list of integers
        a (int):    a number with which to compare the elements of lst
    Returns:
        int: the smallest number of lst that is greater than a, or -1 if it does not exist
    """
    min_diff, res = float("inf"), -1
    for num in lst:
        if num > a and num - a < min_diff:
            min_diff = num - a
            res = num

    return res


def test_1():
    assert minimum_greater([3, 7, 12, 20, 21, 25], 5) == 7


def test_2():
    assert minimum_greater([10, 20, 30], 0) == 10


def test_3():
    assert minimum_greater([10, 20, 30], 50) == -1


def test_4():
    assert minimum_greater([], 0) == -1


def test_5():
    assert minimum_greater([1], 0) == 1


def test_6():
    assert minimum_greater([1], 1) == -1


def test_7():
    assert minimum_greater([-1, -2, -3, -4, -5], -3) == -2


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    print("All tests passed.")
