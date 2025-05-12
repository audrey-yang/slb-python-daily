"""
T-Shirt Sizes

Difficulty: Easy

Given a 2D list containing product id and size of t-shirts in that order. Sort the entries on the basis of size in ascending order. Size is mentioned as S, M, L, XL, XXL or XXXL.

Examples:

Test Case 1:
Input - [[111222, 'L'], [222551, 'XL'], [213243, 'S']]
Output - [[213243, 'S'], [111222, 'L'], [222551, 'XL']]
Explanation - Size S < Size L < Size XL
"""

import math


def sort_shirts(products: list[list]):
    """
    Sorts list of [product_id, shirt_size] by ascending shirt size. 
    Shirt size order is S, M, L, XL, XXL, XXXL.

     Args:
        products: List shirts represented as [product_id: int, shirt_size: str]

    Returns:
        list[list]: The sorted list of products. If a certain size is not defined, it is inserted at the end.
    """
    shirt_to_num = {
        'S': 0,
        'M': 1,
        'L': 2,
        'XL': 3,
        'XXL': 4,
        'XXXL': 5
    }
    return sorted(
        products, key=lambda entry: shirt_to_num.get(entry[1], math.inf)
    )


def test_1():
    assert sort_shirts([[111222, 'L'], [222551, 'XL'], [213243, 'S']]) == [
        [213243, 'S'], [111222, 'L'], [222551, 'XL']]


def test_2():
    assert sort_shirts([[0, 'L'], [1, 'XL'], [2, 'S'], [3, 'XXL'], [3, 'M']]) == [
        [2, 'S'], [3, 'M'], [0, 'L'], [1, 'XL'], [3, 'XXL']]


def test_3():
    assert sort_shirts([]) == []


def test_4():
    assert sort_shirts([[0, 'L'], [1, 'XS']]) == [[0, 'L'], [1, 'XS']]


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    print("All tests passed.")
