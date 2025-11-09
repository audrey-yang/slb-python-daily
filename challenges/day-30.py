"""
Frequency Filter II
Difficulty: Medium

Given a list of numbers and a number k, find the k most frequent elements in the list. Return a list of those numbers. Order of the numbers doesn't matter.

Example:

Test Case 1:
Input - [1,2,2,2,1,1,1,3], 2
Output - [1,2]
Explanation - 1 and 2 are the 2 most frequently occurring numbers.

Test Case 2:
Input - [2,2,2,1,1,5,5,1,4,5,2,3,1,3], 3
Output - [2,5,1]
Explanation - 1,2 and 5 are the 3 most frequently occurring numbers.
"""
from collections import Counter


def frequency_filter(nums: list[int], k: int) -> list[int]:
    return [entry[0] for entry in Counter(nums).most_common(k)]


def test_1():
    assert set(frequency_filter([1, 2, 2, 2, 1, 1, 1, 3], 2)) == set([1, 2])


def test_2():
    assert set(frequency_filter(
        [2, 2, 2, 1, 1, 5, 5, 1, 4, 5, 2, 3, 1, 3], 3)) == set([1, 2, 5])


def test_3():
    assert set(frequency_filter([1, 2, 3, 4, 5], 2)) == set([1, 2])


def test_4():
    assert set(frequency_filter([1, 1, 1, 1, 1, 1, 1], 2)) == set([1])


def test_5():
    assert set(frequency_filter([], 2)) == set()


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
