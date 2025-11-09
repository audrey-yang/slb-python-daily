"""
Elimination Walk
Difficulty: Medium
Given a list of numbers, remove alternate elements starting from the first one. Return the list with the remaining elements. The numbers in output should be in the same order as they were in the given list. Use recursion to perform the task. Note - Don't use loops.

Examples:
Test Case1:
Input: [1,2,3,4,5]
Output: [2,4]
Explanation: 1, 3 and 5 have been removed. Only 2, 4 remain. So, [2,4] is returned.

Test Case 2:
Input: [5,3,7,11,6,8]
Output: [3,11,8]
Explanation: 5,7 and 6 were removed. So, [3, 11, 8] is the output.
"""


def elimination_walk(lst: list[int]) -> list[int]:
    """
    Removes alternate elements starting from the first one and returns the list with the remaining elements

    Args:
        lst: List of integers

    Returns:
        list[int]: The list with alternate elements removed
    """
    return lst[1::2]


def elimination_walk_recursive(lst: list[int]) -> list[int]:
    """
    Removes alternate elements starting from the first one and returns the list with the remaining elements

    Args:
        lst: List of integers

    Returns:
        list[int]: The list with alternate elements removed
    """
    if len(lst) <= 1:
        return []
    return [lst[1]] + elimination_walk_recursive(lst[2:])


def test_1():
    assert elimination_walk([1, 2, 3, 4, 5]) == [2, 4]
    assert elimination_walk_recursive([1, 2, 3, 4, 5]) == [2, 4]


def test_2():
    assert elimination_walk([5, 3, 7, 11, 6, 8]) == [3, 11, 8]
    assert elimination_walk_recursive([1, 2, 3, 4, 5]) == [2, 4]


def test_3():
    assert elimination_walk([]) == []
    assert elimination_walk_recursive([]) == []


def test_4():
    assert elimination_walk([1]) == []
    assert elimination_walk_recursive([1]) == []


def test_5():
    assert elimination_walk([1, 2]) == [2]
    assert elimination_walk_recursive([1, 2]) == [2]


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
