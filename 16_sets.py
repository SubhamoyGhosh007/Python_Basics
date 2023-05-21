s = {2 , 4 , 2 , 6}  #no repetition of duplicate item.
print(s)
print(len(s))

# print(s[0]) #error

me = set()  #empty set //   // me = {} is empty dictionary

for i in s:
    print(i)



s1 = { 1 , 2 , 4 , 5 , 6}
s2 = {2 , 7 , 8 , 9 , 0 , 1}
s3 = set()

print(s1.union(s2))

print(s1.intersection(s2))
print(s2.intersection(s1))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1 , s2)

s1.update(s2)
print(s1 , s2)
print(s1.intersection(s2))
print(s1.difference(s2))

s3 = {4}
s4 = {4}
print(s3.difference(s4)) ##Empty set set()

s5 = "5"
print(s4.isdisjoint(s5))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s2.issubset(s1))

s4.add(6)
s4.add("6")   #"6" is not equal to 6
print(s4)

s4.discard(6)
print(s4)

item = s4.pop()
print(item)

item = s4.pop()
print(item)
print(s4)

s3.clear()
print(s3)