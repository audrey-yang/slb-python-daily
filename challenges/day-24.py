"""
Collage
Difficulty: Hard
You are given a list of words 'data' and a target word. You want to create the target word using the characters in the words provided in the list 'data'. Return a list of words which can be used to create the target word. If characters in words of data are not enough to create the target word, return an empty list.
Note - Try to use as few words as possible.

Examples:

Test Case 1:

Input - ['work', 'fine', 'powder', 'garbage'], 'wonder'
Output - ['powder', 'fine']
Explanation - The characters w, o, d, e, and r can be taken from powder and 'n' can be taken from fine.

Test Case 2:

Input - ['pen', 'show','drone', 'garbage'], 'garden'
Output - ['drone', 'garbage']
Explanation - The characters d, r, e, and n can be taken from the word drone. 'g' and 'a' can be taken from the word garbage.
"""
from collections import Counter
import math


def collage(data: list[str], word: str) -> list[str]:
    available_chars = Counter()
    counters = [Counter(d) for d in data]

    for i in range(len(data)):
        available_chars += counters[i]

    word_count = Counter(word)
    if not word_count <= available_chars:
        return []

    min_guess = math.inf
    min_inds = []

    # Helper method for backtracking
    def search(guess, size, inds, i):
        nonlocal min_guess, min_inds
        if word_count <= guess:
            if size < min_guess:
                min_guess = size
                min_inds = inds
            return

        for j in range(i + 1, len(data)):
            search(guess + counters[j], size + 1, inds + [j], j)

    for i in range(len(data)):
        search(counters[i], 1, [i], i)

    return [data[i] for i in min_inds]


def test_1():
    assert set(collage(['work', 'fine', 'powder', 'garbage'], 'wonder')) == set(
        ['powder', 'fine'])


def test_2():
    assert set(collage(['pen', 'show', 'drone', 'garbage'],
               'garden')) == set(['drone', 'garbage'])


def test_3():
    assert set(collage(['pen'], 'garden')) == set()


def test_4():
    assert set(collage([], 'a')) == set()


def test_5():
    assert set(collage(['pen', 'show', 'drone', 'garbage'],
               'drone')) == set(['drone'])


def test_6():
    assert set(collage(['a', 'b', 'c', 'd', 'abcd'],
               'abcd')) == set(['abcd'])


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    print("All tests passed.")
