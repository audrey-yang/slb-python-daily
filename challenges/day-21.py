"""
Problem
Confusion by Recursion
Difficulty: Medium

What is the function of the following code snippet, and what type of list does it take as input?

Code:


 def func(a, item, segment_start_index = 0):
   if len(a) > 0 and a[-1] < item:
       return -1
   if a[0] == item:
       return segment_start_index+1
   first = func(a[:len(a)//2], item, segment_start_index)
   second = func(a[len(a)//2:], item, segment_start_index+len(a)//2)

   if first != -1:
       return first
   elif second != -1:
       return second

   return -1

 print(func([1,3,5,6,7,9], 10, 0))


Options:
- Binary Search, Any Type of List
- Merge Sort, Any Type of List
- Linear Search, Any Type of List
X None of the above
"""


def func(a, item, segment_start_index=0):
    if len(a) > 0 and a[-1] < item:
        return -1
    if a[0] == item:
        return segment_start_index+1
    first = func(a[:len(a)//2], item, segment_start_index)
    second = func(a[len(a)//2:], item, segment_start_index+len(a)//2)

    if first != -1:
        return first
    elif second != -1:
        return second

    return -1


"""
X None of the above

This function does a binary search. By definition, it will only work on a sorted list.
"""


def test_1():
    assert func([1, 3, 5, 6, 7, 9], 10, 0) == -1


def test_2():
    assert func([1, 3, 5, 6, 7, 9], 6, 0) == 4


def test_3():
    assert func([1, 3, 5, 6, 7, 9], 1, 0) == 1


def test_4():
    # doesn't work on non-sorted lists!
    error_was_thrown = False
    try:
        func([1, 3, 5, 6, 7, 2, 4], 2, 0)
    except Exception:
        error_was_thrown = True
    assert error_was_thrown is True


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    print("All tests passed.")
