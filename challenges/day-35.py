"""
Problem: Sliding Window Maximum

Difficulty: Hard
Given an array and a window size k, find the maximum element in each sliding window as it moves from left to right. Write a python code and return list of maximums.

Examples:
Test Case 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3, 3, 5, 5, 6, 7]
Explanation:
Window [1,3,-1] max=3, [3,-1,-3] max=3, [-1,-3,5] max=5,
[-3,5,3] max=5, [5,3,6] max=6, [3,6,7] max=7

Test Case 2:
Input: nums = [9,8,7,6,5], k = 2
Output: [9, 8, 7, 6]
"""

import heapq

def sliding_window_max(arr, k):
    assert len(arr) >= k
    res = []
    heap = [(-arr[i], i) for i in range(k)]
    heapq.heapify(heap)

    for i in range(k, len(arr) + 1):
        while heap[0][1] < i - k:
            heapq.heappop(heap)
        res.append(-heap[0][0])
        
        if i < len(arr):
            heapq.heappush(heap, (-arr[i], i))
    
    return res

def test_1():
    assert sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7]

def test_2():
    assert sliding_window_max([9,8,7,6,5], 2) == [9, 8, 7, 6]

def test_3():
    assert sliding_window_max([1], 1) == [1]

def test_4():
    assert sliding_window_max([1,2,3,4,5], 1) == [1,2,3,4,5]

def test_5():
    assert sliding_window_max([1,2,3,4,5], 2) == [2,3,4,5]


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
