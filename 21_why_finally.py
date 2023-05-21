def func1():
    a = input("Enter the number : ")
    try:
        print(int(a))
        return 1
    except Exception as e:
        return e
    print("I will execute")  # This line will never be executed

def func2():
    a = input("Enter the number : ")
    try:
        print(int(a))
        return 1
    except Exception as e:
        return e
    finally:
        print("I will execute")

func1()
func2()