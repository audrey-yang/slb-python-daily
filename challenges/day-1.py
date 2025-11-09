"""
Problem - Words
Difficulty: Medium

Question: The words in a paragraph were stored in a 2D list. Each list inside the given list corresponds to a sentence. The elements of this list are words of that sentence. You have to find the mean number of words in each sentence; write a python function to perform this task. 
The mean of n values x1,x2…,xn=(∑xi)/n. Round off the result to 2 decimal places.

Examples:
- Test Case 1:
    Input - [['I', 'am', 'hungry'], [“Let's”, 'order']]
    Output - 2.5
    Explanation - The first sentence has 3 words. The second one has 2. Mean = (3+2)/2 = 2.5

- Test Case 2:
    Input - [['We', 'know', 'what', 'we', 'are'], ['But', 'know', 'not', 'what', 'we', 'may', 'be']]
    Output - 6.0
    Explanation - First sentence has 5 words. Second has 7 words. Mean = 6.
"""


def mean_number_of_words(paragraph: list[list[str]]) -> float:
    """
    Calculate the mean number of words in each sentence of a paragraph.

    Args:
        paragraph: A 2D list where each inner list represents a sentence.
    Returns:
        float: The mean number of words in the sentences, rounded to 2 decimal places.
    """
    if not paragraph:
        return 0.00

    return round(sum(map(lambda sent: len(sent), paragraph)) / len(paragraph), 2)


def test_1():
    input = [['I', 'am', 'hungry'], ['Let\'s', 'order']]
    assert mean_number_of_words(input) == 2.50


def test_2():
    input = [['We', 'know', 'what', 'we', 'are'], [
        'But', 'know', 'not', 'what', 'we', 'may', 'be']]
    assert mean_number_of_words(input) == 6.00


def test_3():
    input = [['We', 'know', 'what', 'we', 'are'], ['But', 'know', 'not',
                                                   'what', 'we', 'may', 'be'], ['We', 'are', 'the', 'champions']]
    assert mean_number_of_words(input) == 5.33


def test_4():
    input = []
    assert mean_number_of_words(input) == 0.00


def test_5():
    input = [['Hello', 'world']]
    assert mean_number_of_words(input) == 2.00


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
