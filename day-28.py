"""
Variable incorrigible
Difficulty: Medium

You are given to decipher the meaning of the following code:

class A:
   def func1(self, a, **kwargs):
       if a == 2:
           print("Ping")
       elif a == 5:
           print("Pong")

   def func2(self, **kwargs):
       if kwargs.get("a") == 2:
           print("Ping")
       else:
           print("Pong")

ob = A()
ob.func1(2, a=5)
ob.func2(a=1, a=2)
"""


class A:
    def func1(self, a, **kwargs):
        if a == 2:
            print("Ping")
        elif a == 5:
            print("Pong")

    def func2(self, **kwargs):
        if kwargs.get("a") == 2:
            print("Ping")
        else:
            print("Pong")


def run():
    ob = A()

    '''
    This call attempts to set `a` both positionally and through a keyword. It will cause a TypeError while running because Python will realize that `a` is set twice.
    '''
    try:
        ob.func1(2, a=5)
    except TypeError as e:
        print("func1 threw a TypeError:", e)

    '''
    This call attempts to pass two values associated with keyword `a`. It causes a SyntaxError (keyword argument repeated), and the code will not run. 
    '''
    # ob.func2(a=1, a=2)


if __name__ == "__main__":
    run()
    print("Done")
