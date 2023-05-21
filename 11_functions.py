def sum(a , b):
    print(a + b)


def add(a , b):
    return (a+b)

def minus (b  , a = 1):
    return (b-a)

def mult(a , b):
    pass

a = int(input("Enter Number : "))
b = int(input("Enter Number : "))

print("Sum is : " )
sum(a,b)

print("Sum is : "  , add(a , b))
print("Sub is : "  , minus(a , b))


