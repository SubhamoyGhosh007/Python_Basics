
'''
dict = {
    key : value , 
    key : value.....
}'''
dic = {
    "Me": "Subhamoy",
    "You": "idk",
    123: "hui"
}


print(dic["Me"])
print(dic["You"])
print(dic[123])
print(dic.get('Me'))
# print(dic["123"]) error
print(dic.get("123"))  # will show none

print(dic.keys())

for keys in dic:
    print(keys)

print(dic.values())

for keys in dic:
    print(f"The value corresponding to the key {keys} is {dic.get(keys)}")


print(dic.items())

for keys,values in dic.items():
    print(f"The value corresponding to the key {keys} is {values}")


ep1 = {
    123 : 45 , 
    124 : 46,
    125 : 80,
    126 : 90
}
ep2 = {
    222 : 67,
    566 : 90
}

ep1.update(ep2)
print(ep1.items())
# ep1.clear()
# print(ep1.items())

ep1.pop(125)
print(ep1.items())

del ep2
ep2 = {
    222 : 67,
    566 : 90
}

for values in ep2.values():
    ep2.popitem

ep2 = {
    222 : 67,
    566 : 90
}

del ep2[222]
ep1.popitem()  #Last key value pair will be poped
print(ep1.items())
# print(ep2.items())  Error
print(ep2.items())

ep2 = {
    222 : 67,
    566 : 90
}
