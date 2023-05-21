from math import sqrt
from functools import reduce
#map
def cube(x):
    return x * x * x


l = [1, 2, 3, 4, 5]
newl = []

for item in l:
    newl.append(cube(item))
print(newl)

newl1 =list(map(cube, l))  #map returns map object
print(newl1)

#filter
def filter_func(a):
    return a > 10

newl2 = list(filter(filter_func, newl1))
print(newl2)

#Reduce

newl3 = reduce(lambda x, y: x+y, l)
print(newl3)