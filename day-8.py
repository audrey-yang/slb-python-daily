"""
What does the following code snippet print?
Difficulty: Medium

Code:

    class A:
        var = 1

    class B(A):
        var = 2

    class C(A):
        var = 3

    ob1 = C()
    ob2 = B()

    print(type(ob1) == type(A), isinstance(ob2, A))

 
Options:
- True, True
- True, False
X False, True
- False, False

- ob1 is an instance of C, so its type is C. The type of A is "type" since it is a class and all classes are instances of metaclass "type." So, the two returned types are not equal.
- `isinstance` returns True if the ob2 is an instance of A (or any of its subclasses). B is a subclass of A, and ob2 is an instance of B, so ob2 is an instance of A.
"""


class A:
    var = 1


class B(A):
    var = 2


class C(A):
    var = 3


def check_result():
    ob1 = C()
    ob2 = B()

    return type(ob1) == type(A), isinstance(ob2, A)


if __name__ == "__main__":
    assert check_result() == (False, True)
    print("All tests passed.")
