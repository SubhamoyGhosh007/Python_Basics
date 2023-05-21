import math


def func(fx, value):
    return fx(value) + 6


def fx(value):
    return value * math.sqrt(value)


print(func(fx, 36))


#Doing same using lambda

def f1(f2, value):
    return value + f2(value)

print(f1(lambda x : x + 2, 2))
