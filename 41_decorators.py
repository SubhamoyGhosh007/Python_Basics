def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


# @greet
# def hello():
#     print("Hello")


# hello()

#greet(hello)()
# @greet
def add(a, b, c):
    print(a+b+c)


greet(add)(1 , 2, 3)
# add(1, 2)