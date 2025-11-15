"""
Problem: Binary Tree Level Order

Difficulty: Hard
Given a binary tree as nested lists, return level order traversal (nodes at each depth as separate lists).
Tree format: [value, left_subtree, right_subtree] or None for empty.

Examples:
Test Case 1:
Input: [3, [9, None, None], [20, [15, None, None], [7, None, None]]]
Output: [[3], [9, 20], [15, 7]]
Explanation: Level 0: [3], Level 1: [9, 20], Level 2: [15, 7]

Test Case 2:
Input: [1, [2, None, None], None]
Output: [[1], [2]]
"""

from collections import deque

def level_order(root):
    if not root:
        return []
    
    res = []
    q = deque([root])
    while q:
        layer, len_layer = [], len(q)
        for _ in range(len_layer):
            val, l, r = q.popleft()
            layer.append(val)
            if l:
                q.append(l)
            if r:
                q.append(r)
        res.append(layer)
    return res


def test_1():
    assert level_order([3, [9, None, None], [20, [15, None, None], [7, None, None]]]) == [[3], [9, 20], [15, 7]]

def test_2():
    assert level_order([1, [2, None, None], None]) == [[1], [2]]

def test_3():
    assert level_order([1, None, None]) == [[1]]

def test_4():
    assert level_order(None) == []

def test_5():
    assert level_order([1, [2, [4, None, None], None], [3, [5, None, None], None]]) == [[1], [2, 3], [4, 5]]


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5 ()
    print("All tests passed.")
