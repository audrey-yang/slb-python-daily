"""
Compare Strings
Difficulty: Easy

Question: You are given two strings s1 and s2. Write a program to find which one will come first in alphabetical order. Return that string.

Examples:

Test Case 1:
Input - 'abc', 'abcd'
Output - 'abc'

Test Case 2:
Input - 'pen', 'pineapple'
Output - 'pen'
"""


def compare_strings(s1: str, s2: str) -> str:
    return s1 if s1 <= s2 else s2


def test_1():
    assert compare_strings("abc", "abcd") == "abc"


def test_2():
    assert compare_strings("pen", "pineapple") == "pen"


def test_3():
    assert compare_strings("abc", "") == ""


def test_4():
    assert compare_strings("120c", "119c") == "119c"


def test_5():
    assert compare_strings("abcde", "abcde") == "abcde"


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
