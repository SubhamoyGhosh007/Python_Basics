#Tuple is immmutable

tup = (1)
print(type(tup) , tup)

tup = (1 , )
print(type(tup) , tup)

# tup[0] = 90 <= Error as tuple is immutable 

tuple1 = ("Hello" , "1" , 2  , True)
print(tuple1)
print(tuple1[0])
print(tuple1[3])

print(tuple1[-2])  # tuple1[-2]  = tuple1[len(tuple1) - 2]
print("Using loop")
for c in tuple1 :
    print(c)

if 2 in tuple1:
    print("Present")
else:
    print("Absent")

# Slicing
tup2 = tuple1[1 : 4]   # ( 1 2 3 )   [by default = (0 : length)]
print(tup2)

i =0

for c in tuple1:
    i = i + 1

print(i)
tuple2 = (0,1,4,0,1,2,4,1)
i = tuple2.count(0)
print("Number is occurance of zero in tuple2 is : " , i)
print(tuple2.index(4))
print(tuple2.index(4 , 3 , 7))