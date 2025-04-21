"""
Over here
Difficulty: Easy
Given a list of integers, find a number in it which satisfies the equation $$x^2 - 14x + 40$$. If none of the numbers satisfy, return -1.

Examples:

Test Case 1:
Input: [3,2,1,4,6,8]
Output: 4
Explanation: If we put 4 in the equation, we get $4^2 - 14*4 + 40 = 16 - 56 + 40 = 0$. So, 4 satisfies the equation.

Test Case 2:
Input: [100,20,30,40,50]
Output: -1
Explanation: None of the numbers in the list satisfy the equation, so we return -1.
"""


def satisfy_equation(lst: list[int]) -> int:
    """
    Finds a solution to the equation $$x^2 - 14x + 40 = 0$$ from the given list of integers. Note that the factorization of this equation comes to $$(x - 4)(x - 10)$$, which means the only solutions are 4 and 10.

    Args:
        lst (list[int]): A list of integers
    Returns: 
        int: An integer from the list that satisfies the equation, or -1 if none do
    """
    return 10 if 10 in lst else 4 if 4 in lst else -1


def test_1():
    assert satisfy_equation([3, 2, 1, 4, 6, 8]) == 4


def test_2():
    assert satisfy_equation([100, 20, 30, 40, 50]) == -1


def test_3():
    assert satisfy_equation([]) == -1


def test_4():
    assert satisfy_equation([10, 4, 10]) == 10


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    print("All tests passed.")
