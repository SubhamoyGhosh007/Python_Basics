def fact(a):
    if(a >= 1):
        return (a * fact(a-1))
    else:
        return 1

a = int(input("Enter the number : "))
if(a >= 0):
    print("Factorial of ",a," is : " , fact(a))
else:
    print("Factorial of -ve numbers are not possible.")