"""
Reverse In Place

Difficulty: Medium
You are given a list of numbers. Write a program to reverse the list, while using $O(1)$ extra space.

Examples:

Test Case 1:
Input - [1,2,3,4,5]
Output - [5,4,3,2,1]
Explanation - The list has been reversed.
"""


def reverse_list(lst: list):
    '''Reverses a list in-place using built-in list operators'''
    lst[:] = lst[::-1]


def reverse_list2(lst: list):
    '''Reverses a list in-place without list operators'''
    l, r = 0, len(lst) - 1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        l += 1
        r -= 1


def test_1(rev):
    lst = [1, 2, 3, 4, 5]
    rev(lst)
    assert lst == [5, 4, 3, 2, 1]


def test_2(rev):
    lst = []
    rev(lst)
    assert lst == []


def test_3(rev):
    lst = [1]
    rev(lst)
    assert lst == [1]


def test_4(rev):
    lst = [1, 2, 3, 4]
    rev(lst)
    assert lst == [4, 3, 2, 1]


if __name__ == "__main__":
    test_1(reverse_list)
    test_2(reverse_list)
    test_3(reverse_list)
    test_4(reverse_list)
    test_1(reverse_list2)
    test_2(reverse_list2)
    test_3(reverse_list2)
    test_4(reverse_list2)
    print("All tests passed.")
