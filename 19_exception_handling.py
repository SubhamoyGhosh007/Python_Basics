try:
    a = int(input("Enter the number : "))
    print(f"Multiplication Table of {a} is ")
    for i in range(1, 11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print(f"Sorry Some error occurred due to ", e)

print(f"End of program\n")
