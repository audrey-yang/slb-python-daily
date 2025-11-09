"""
Problem: Subarray Sum Equals K

Difficulty: Hard
Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals k.

Examples:
Test Case 1:
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: [1,1] appears twice: indices [0,1] and [1,2]

Test Case 2:
Input: nums = [1, 2, 3, 4], k = 5
Output: 1
Explanation: [2,3] and [1,4] both sum to 5 -- wait, [1,4] not continuous Actually: [2,3] at indices [1,2] is one.
"""

from collections import defaultdict

def subarray_sum_equals_k(arr, k):
    assert len(arr) > 0

    prefixes = defaultdict(int)
    prefixes[0] = 1

    num_sum_k = 0
    running = 0

    for num in arr:
        running += num
        if prefixes[running - k] > 0:
            num_sum_k += prefixes[running - k]
        prefixes[running] += 1
        
    return num_sum_k

def test_1():
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2

def test_2():
    assert subarray_sum_equals_k([1, 2, 3, 4], 5) == 1

def test_3():
    assert subarray_sum_equals_k([1, -1, 1, -1, 1, -1], 0) == 9

def test_4():
    assert subarray_sum_equals_k([1, 1, 1], 5) == 0

def test_5():
    assert subarray_sum_equals_k([1], 1) == 1


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
