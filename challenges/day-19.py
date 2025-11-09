"""
Curve Ball
Difficulty: Medium
Question: What will be the output of the following piece of code?

```python
total = 0
for i in range(1, 15/3):
    total += i
print(total)
```
"""


def run():
    total = 0
    for i in range(1, 15/3):
        total += i
    print(total)


"""
This piece of code throws a TypeError, as the `range` function only accepts integers as arguments. Since `/` returns a float, `15/3` is not a valid argument to `range`.
"""


def test():
    exception_was_thrown = False
    try:
        run()
    except TypeError:
        exception_was_thrown = True

    assert exception_was_thrown is True


if __name__ == "__main__":
    test()
    print("All tests passed.")
