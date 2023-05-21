while(True):
    a = float(input("Enter First Number : "))
    b = float(input("Enter Second Number : "))
    ch = input("Enter the operator \nOptions :   '+','-','*','/','%','**' : ")
    

    match ch:
        case "+" : print("Sum of" , a , " and " , b , " is :  " , a + b)
        case "-" : print("Substraction of" , a , " and " , b , " is :  " , a - b)
        case "*" : print("Multiplication of" , a , " and " , b , " is :  " , a * b)
        case "/" : 
            if(b == 0):
                print("Error : Denomerator is zero !")
            else:
                print("Division  of" , a , " and " , b , " is :  " , a / b)
        case "%" : 
            if(b == 0):
                print("Error : Denomerator is zero !")
            else:
                print("Remainder of" , a , " and " , b , " is :  " , a % b)
        case "^" : print("Exponential of" , a , " to " , b , " is :  " , a ** b)
        case _ : print("Use the right syntax")

   
    cont = input("Do you want to continue ?(Y/N) : ")
    if(cont == "N"):
        break

