"""
Problem: Character Frequency Map

Difficulty: Medium
Given a string, create a dictionary where keys are characters and values are their frequencies. Return only characters that appear more than once. Ignore spaces and make it case-insensitive.

Examples:
Test Case 1:
Input: "Hello World"
Output: {'l': 3, 'o': 2}
Explanation: 'l' appears 3 times, 'o' appears 2 times (case-insensitive)

Test Case 2:
Input: "Programming"
Output: {'r': 2, 'g': 2, 'm': 2}
Explanation: r, g, and m each appear twice
"""

def character_frequency_map(s):
    seen = set()
    final = {}
    for c in s.lower():
        if c not in seen:
            seen.add(c)
        else:
            final[c] = final.get(c, 1) + 1 
    return final


def test_1():
    assert character_frequency_map("Hello World") == {'l': 3, 'o': 2}

def test_2():
    assert character_frequency_map("Programming") == {'r': 2, 'g': 2, 'm': 2}

def test_3():
    assert character_frequency_map("aA aA bBb c...") == {'a': 4, 'b': 3, '.': 3, ' ': 3}

def test_4():
    assert character_frequency_map("abcde") == {}

def test_5():
    assert character_frequency_map("") == {}


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
