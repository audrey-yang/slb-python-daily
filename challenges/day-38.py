"""
Problem: Majority Element

Difficulty: Easy
Given an array, find the majority element (appears more than n//2 times). You can assume the majority element always exists.

Examples:
Test Case 1:
Input: [3, 2, 3]
Output: 3
Explanation: 3 appears 2 times out of 3 elements (more than 1.5)

Test Case 2:
Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: 2 appears 4 times out of 7 (more than 3.5)
"""

def majority_element(arr):
    majority, count = 0, 0

    for num in arr:
        if count == 0:
            majority = num
        count += (1 if num == majority else -1)

    return majority


def test_1():
    assert majority_element([3, 2, 3]) == 3 

def test_2():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

def test_3():
    assert majority_element([1, 2, 3, 2, 1, 1]) == 1

def test_4():
    assert majority_element([1]) == 1


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    print("All tests passed.")