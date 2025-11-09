"""
Difference Pairs

Difficulty: Medium

You are given a list 'data', and a non-negative number 'd'. Find the number of unique pairs in data whose difference is d. Try to do this in O(n log n) time complexity.

Examples:

Test Case 1:
Input - [1,2,5,3], 1
Output - 2

Explanation - Pairs 1,2 and 2,3 have difference of 1. So, 2 is returned.

Test Case 2:

Input - [1,5,5,3,0], 4
Output - 1
Explanation - 1,5 is the only unique pair with difference 4.
"""


def number_of_pairs_with_diff(data: list[int], d: int) -> int:
    """Finds the number of unique pairs in input list data with difference d"""
    d = abs(d)
    data.sort()

    pairs = set()
    seen = set()
    for num in data:
        if num - d in seen:
            pairs.add((min(num, num - d), max(num, num - d)))
        seen.add(num)

    return len(pairs)


def test_1():
    assert number_of_pairs_with_diff([1, 2, 5, 3], 1) == 2


def test_2():
    assert number_of_pairs_with_diff([1, 5, 5, 3, 0], 4) == 1


def test_3():
    assert number_of_pairs_with_diff([], 1) == 0


def test_4():
    assert number_of_pairs_with_diff([1, 10, 15], 3) == 0


def test_5():
    assert number_of_pairs_with_diff([1, 5, 5, 3, 0], -4) == 1
    assert number_of_pairs_with_diff([5, 5, 3, 0, 1], -4) == 1


def test_6():
    assert number_of_pairs_with_diff([1, 1, 1, 1, 1], 0) == 1


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    print("All tests passed.")
