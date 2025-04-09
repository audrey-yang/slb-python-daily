"""
Kaprekarian riddles
Difficulty: Medium

Question: Kaprekar numbers are a special kind of numbers whose repeated sum of digits always add up to either 1 or 9. For example: 6174 => 6 + 1 + 7 + 4 = 18 => 1 + 8 = 9 As you can see, this was done in two steps. Your task is to complete the function with the definition solve_kaprekar(number: int, max_steps: int), which returns whether the function comes out to be a Kaprekar Number within the number of steps less than or equal to max_steps, and return either True or False.

Examples:
Test Case 1:
Input: number=1, max_steps=3
Output: True
Explanation: 1 is a Kaprekar number since the sum of its digits is 1. So we return True

Test Case 2:
Input: number=1674, max_steps=1
Output: False
Explanation: 1+6+7+4 = 18 (Step 1)
1 step has been completed, and the sum of digits hasn't been 1 or 9. So we stop execution here, and return False

Test Case 3:
Input: number=93, max_steps=4
Output: False
Explanation: 9+3=12 (Step 1), 1+2 = 3 (Step 2)
"""

def solve_kaprekar(number: int, max_steps: int) -> bool:
    """
    Determine whether the function comes out to be a Kaprekar Number within the number of steps less than or equal to max_steps

    Args:
        number: The number to check
        max_steps: The upper limit on number of steps
    Returns:
        float: The mean number of words in the sentences, rounded to 2 decimal places.
    """

    def sum_digits(n: int) -> int:
        """Helper function to sum the digits of a number n"""
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    for _ in range(max_steps):
        number = sum_digits(number)
        if number == 1 or number == 9:
            return True
        if number < 10:
            return False
    
    return False

def test_1():
    assert solve_kaprekar(1, 3) is True

def test_2():
    assert solve_kaprekar(1674, 1) is False

def test_3():
    assert solve_kaprekar(1674, 2) is True

def test_4():
    assert solve_kaprekar(93, 4) is False

def test_5():
    assert solve_kaprekar(18, 1) is True

def test_6():
    assert solve_kaprekar(7, 1600) is False

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    print("All tests passed.")
