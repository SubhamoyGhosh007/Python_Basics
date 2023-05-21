# String Formatting

letter1  = "Hello I am {} , I am from {}"
print(letter1.format("Subhamoy" , "Agarpara"))

letter2  = "Hello I am {} , I am from {}"
name = "Subhamoy"
place  = "Agarpara"

print(letter2.format(name , place))
print(letter2.format(place , name))

letter2  = "Hello I am {1} , I am from {0}"
print(letter2.format(place , name))

#f-string
name = input("Enter name : ");
place = input("Enter place : ");
letter3 = f"Hello I am {name} , I am from {place}"
print(letter3)

price = float(input("Enter price  : "))
txt = f"This is of {price : .2f} RS"
print(txt)

#retain your fstring

txt = f"This is of {{price : .2f}}RS"
print(txt)
