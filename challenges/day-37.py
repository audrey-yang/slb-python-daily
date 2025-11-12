"""
Problem: String Permutations Check
Difficulty: Medium

Given two strings s1 and s2, check if s2 contains any permutation of s1. In other words, check if one of s1's permutations is a substring of s2.

Examples:
Test Case 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: True
Explanation: s2 contains "ba" which is a permutation of "ab"

Test Case 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: False
Explanation: No permutation of "ab" exists as substring in s2
"""

from collections import Counter

def is_permutation(s1, s2):
    s1_freqs = Counter(s1)
    window_freqs = Counter(s2[:len(s1)])
    l, r = 0, len(s1)

    while r < len(s2):
        if s1_freqs == window_freqs:
            return True
        window_freqs[s2[l]] -= 1
        window_freqs[s2[r]] += 1
        l, r = l+1, r+1
        window_freqs -= Counter()
    
    return s1_freqs == window_freqs

def test_1():
    assert is_permutation("ab", "eidbaooo") 

def test_2():
    assert not is_permutation("ab", "eidboaoo") 

def test_3():
    assert is_permutation("a", "a") 

def test_4():
    assert is_permutation("", "eidbaooo") 

def test_5():
    assert not is_permutation("abcdefg", "abcdef") 


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")