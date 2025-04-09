"""
Problem - Wasted Nested
 
Difficulty: Medium
 
Question: Nested functions are a big deal breaker in Object Oriented Programming. It's not recommended to use them usually, unless some different case arises. 
That said, can you convert this nested function func1 into a non-nested function?
 
 
 def func1(power, number=78):
   def square(x):
       return x*x
   def cube(x):
       return x**3
   if power == 2:
       return square(number)
   elif power == 3:
       return cube(number)
   else:
       print("Unknown power")
       return -1

 
Example:

 def func1():
   def b():
       print("Hi")
       b()

 
Can be simply nested into:

 def func1():
   print("Hi")
"""

from random import randint


def func1(power, number=78):
   def square(x):
       return x*x
   def cube(x):
       return x**3
   if power == 2:
       return square(number)
   elif power == 3:
       return cube(number)
   else:
       print("Unknown power")
       return -1
   
def func1_revised(power, number=78):
    if power == 2 or power == 3:
        return number ** power
    print("Unknown power")
    return -1

def test_1():
    x = randint(-100, 100)
    assert func1_revised(0, x) == func1(0, x)
    assert func1_revised(1, x) == func1(1, x)
    assert func1_revised(4, x) == func1(4, x)

def test_2():
    x = randint(-100, 100)
    assert func1_revised(2, x) == func1(2, x)

def test_3():
    x = randint(-100, 100)
    assert func1_revised(3, x) == func1(3, x)

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    print("All tests passed.")
