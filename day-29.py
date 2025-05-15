"""
Tail match
Difficulty: Hard
Question: Given a list of integers, group all numbers which end with the same digit and return as a dictionary. The keys of the dictionary will be the last digit and value of dictionary will be a list of numbers. If given list is empty return -1.

Examples:
Test Case 1:
Input - [5, 10, 15, 4, 50]
Output - {5: [5,15], 0: [10, 50], 4: [4]}
Explanation - 5 and 15 end with 5, so they are grouped together. 10 and 50 end with 0. 4 ends with 4.

Test Case 2:
Input - [22,3,22,2,71,11]
Output - {2: [22, 22, 2], 3: [3], 1: [71, 11]}
Explanation - 22, 22 and 2 end with 2, so they are grouped together. 3 ends with 3. 71 and 11 end with 1.
"""
from collections import defaultdict


def tail_match(nums: list[int]) -> dict:
    res = defaultdict(list)
    for num in nums:
        res[abs(num) % 10].append(num)
    return res or {-1: []}


def test_1():
    assert tail_match([5, 10, 15, 4, 50]) == {5: [5, 15], 0: [10, 50], 4: [4]}


def test_2():
    assert tail_match([22, 3, 22, 2, 71, 11]) == {
        2: [22, 22, 2], 3: [3], 1: [71, 11]}


def test_3():
    assert tail_match([]) == {-1: []}


def test_4():
    assert tail_match([1, 1, 2]) == {1: [1, 1], 2: [2]}


def test_5():
    assert tail_match([-1, 1, 2]) == {1: [-1, 1], 2: [2]}


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
