f = open("myFile.txt", "r")  # r mode is default and same as rt
print(f.read())
# text = f.read()  same as above
# print(text)
f.close()

f1 = open("myFile1.txt", "w")

# print(f1.read())  You cannot read a file in write mode
f1.close()


f2 = open("myFile3.txt", "w")  # w mode will create a file if the file does not exist
f2.close()

f1 = open("myFile.txt", "rb")  #rb for read in binary mode
print(f1.read())
f1.close()

# f2 = open("myFile1.txt", "w")
# f2.write("Yo bro love you")  #It will replace the whole text
# f2.close()

f2 = open("myFile1.txt", "a")
f2.write("\nHEHE")  #It will append the text
f2.close()
