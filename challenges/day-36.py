"""
Problem: Armstrong Number Checker

Difficulty: Easy
An Armstrong number is a number equal to the sum of its digits each raised to the power of the number of digits. Check if given number is Armstrong.

Examples:
Test Case 1:
Input: 153
Output: True
Explanation: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

Test Case 2:
Input: 9474
Output: True
Explanation: 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474
"""

import math

def is_armstrong_number(num):
    if num == 0:
        return False
    
    num_digits = int(math.log10(abs(num))) + 1
    digits, sum_digits = num, 0
    while digits > 0:
        sum_digits += (digits % 10) ** num_digits
        digits //= 10
    
    return num == sum_digits

def test_1():
    assert is_armstrong_number(153)

def test_2():
    assert is_armstrong_number(9474)

def test_3():
    assert is_armstrong_number(1)

def test_4():
    assert not is_armstrong_number(10)

def test_5():
    assert not is_armstrong_number(36)


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")