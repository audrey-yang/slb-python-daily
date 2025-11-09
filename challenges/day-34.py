"""
Problem: What's the output?
 
Difficulty: Medium
What is the output of the following code?

```
def outer():   
    x = "outer"   
    def inner():       
        nonlocal x       
        x = "inner"       
        print(x)   
    inner()   
    print(x)

outer()
```

Options:
A. outer, outer
B. inner, inner
C. inner, outer
D. Error
"""

"""
Answer: B. inner, inner

In the function `inner`, we specify `nonlocal x` to use `x` as a global variable. Therefore, it is the same variable that `outer` has. `inner` modifies `x` to `"inner"` and because it is the same variable that `outer` has and the print is after the update, `outer` prints the updated value.
"""

def outer():   
    x = "outer"   
    def inner():       
        nonlocal x       
        x = "inner"       
        print(x)   
    inner()   
    print(x)


if __name__ == "__main__":
    outer()
    print("Solution: B. inner, inner")
