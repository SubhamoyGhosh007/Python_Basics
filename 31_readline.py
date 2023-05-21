# f = open("myFile3.txt", "r")
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break


f = open("marks.txt", "r")
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]   #split returns  substring
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in ENVS is: {m2}")
    print(f"Marks of student {i} in CS is: {m3}")
