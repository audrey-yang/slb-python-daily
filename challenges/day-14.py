"""
Locate Peak

Difficulty: Medium

Question: Given a list of integers, find the index of the maximum value. If there are two maximums, return index of the first one. If given list is empty return -1. Do not use the index() method.

Examples:

Test Case 1:
Input - [5, 10, 15, 4, 6]
Output - 2
Explanation - The maximum number is 15. Its index is 2.

Test Case 2:
Input - [22, 3, 22, 2, 7, 11]
Output - 0
Explanation - There are two maximums with value 22. The first one has index 0.
"""


def locate_peak(lst: list[int]) -> int:
    """
    Locates the index of the maximum value in a list of integers. If multiple maxima exist, the index of the first on is returned. If no maximum exists, -1 is returned.

    Args:
        lst (list[int]): A list of integers
    Returns:
        int: The index of the maximum value or -1 if the list is empty
    """
    cur_max, cur_max_ind = float('-inf'), -1
    for i, num in enumerate(lst):
        if num > cur_max:
            cur_max = num
            cur_max_ind = i

    return cur_max_ind


def test_1():
    assert locate_peak([5, 10, 15, 4, 6]) == 2


def test_2():
    assert locate_peak([22, 3, 22, 2, 7, 11]) == 0


def test_3():
    assert locate_peak([]) == -1


def test_4():
    assert locate_peak([-1]) == 0


def test_5():
    assert locate_peak([-1, 2, 3, 3, 3, 2, 3]) == 2


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
