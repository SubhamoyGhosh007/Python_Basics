with open("file.txt", "r") as f:
    print(type(f))
    f.seek(10) #from which'th position the reading will be started
    data = f.read(5)  #How many characters to be read
    print(data)

with open("file.txt", "r") as f:
    print(type(f))
    f.seek(10) #from which'th position the reading will be started
    data = f.read(5)  #How many characters to be read
    print(f.tell()) #returns the bytes is seeked
    print(data)

with open("sample.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5) #truncate n charecters
with open("sample.txt", "r") as f:
    print(f.read())