"""
Problem: Prime Factorization

Difficulty: Medium
Given a positive integer, return a list of its prime factors in ascending order. Include duplicate factors (e.g., 8 = [2, 2, 2]).

Examples:
Test Case 1:
Input: 84
Output: [2, 2, 3, 7]
Explanation: 84 = 2 x 2 x 3 x 7

Test Case 2:
Input: 17
Output: [17]
Explanation: 17 is prime, so it's its own only prime factor
"""

def prime_factorization(num):
    assert num > 1
    factor, factors = 2, []
    while num > 1:
        if num % factor == 0:
            num /= factor
            factors.append(factor)
        else:
            factor += 1
    return factors


def test_1():
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_2():
    assert prime_factorization(17) == [17]

def test_3():
    assert prime_factorization(2) == [2]

def test_4():
    assert prime_factorization(10) == [2, 5]

def test_5():
    assert prime_factorization(16) == [2, 2, 2, 2]

def test_6():
    exception_thrown = False
    try:
        prime_factorization(0)
    except AssertionError:
        exception_thrown = True
    assert exception_thrown


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    print("All tests passed.")
