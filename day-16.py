"""
Operator resolution
Difficulty: Medium

What is the output of the following code? Please post your explanation as well.

```
isinstance(+, Object)
```

Options:
    1. True
    2. False
    X Error
    4. None of the above
"""

import operator
"""
Answer: 3. Error

First of all, the code produces a syntax error, as `+` cannot be applied as an argument to a function.

If we fix the syntax error by using `operator.__add__` (which is the function for addition), the code will still throw an error because there is no such class as `Object` in Python. 
"""


def test_1():
    error_was_thrown = False
    try:
        isinstance(operator.__add__, Object)
    except Exception as e:
        error_was_thrown = True

    assert error_was_thrown is True


"""
But if we correct the code to use `object`, it will return `True`, as Python functions are classes, which all stem from class `object`.
"""


def test_2():
    assert isinstance(operator.__add__, object) is True


if __name__ == "__main__":
    test_1()
    test_1()
    print("All tests passed.")
