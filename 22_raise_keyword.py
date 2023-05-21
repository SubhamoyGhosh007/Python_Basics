try:
    a = int(input("Enter any number between 5 and 9 : "))
    if a < 5 or a > 9:
        raise ValueError("OOPS! Give value between 5 and 9")
    else:
        print(f"Your value is {a}")
except Exception as e:
    print(f"Error occurred due to {e}")
