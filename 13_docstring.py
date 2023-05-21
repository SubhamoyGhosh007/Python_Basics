def square(a) :
    '''Takes a number and return the square value.'''
    return (a**2)

print(square(5))
print(square.__doc__)


def root(a):
    # '''Takes a number and returns square root.'''
    return (a**(0.5))

print(root(36))
print(root.__doc__)  #None


def sum (a , b):
    print("\n")
    '''It takes two numbers and return the sum'''
    return(a +b)

print(sum(4,5))
print(sum.__doc__)  #None, as docstring is mentioned just below the function definition