"""
Problem - Spread
Difficulty: Easy
Given a list of numbers find the spread of the list. Here, spread = Max - Min

Examples:

Test Case 1:
Input: [1,2,3,4,5]
Output: 4
Explanation: Maximum = 5, Minimum = 1. Spread = 5-1 = 4

Test Case 2:
Input: [-1,0,5]
Output: 6
Explanation: Maximum = 5, Minimum = -1. Spread = 5-(-1) = 6.
"""


def spread(numbers: list) -> int:
    """
    Calculate the spread of a list of numbers, where the spread is max - min.

    Args:
        numbers: List of integers

    Returns:
        int: The spread of the list
    """
    assert len(numbers) > 0
    return max(numbers) - min(numbers)


def test_1():
    assert spread([1, 2, 3, 4, 5]) == 4


def test_2():
    assert spread([-1, 0, 5]) == 6


def test_3():
    assert spread([1, 1, 1, 1, 1]) == 0


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    print("All tests passed.")
