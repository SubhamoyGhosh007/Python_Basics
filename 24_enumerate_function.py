marks = [12, 56, 32, 98, 12, 45, 1, 4]
index = 0

for mark in marks:
    print(mark)
    print(f"Nice score sonu") if index == 2 else ""
    index += 1

print(f"\nUsing enumerate function")

for i, mark in enumerate(marks): # i = index and mark =  value
    print(mark)
    print(f"Nice score sonu") if i == 2 else ""

for i, mark in enumerate(marks, start=1): # i = index starting from 1 and mark =  value
    print(mark)
    print(f"Nice score sonu") if i == 2 else ""
