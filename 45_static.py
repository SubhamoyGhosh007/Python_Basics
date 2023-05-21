class Math:
    def __init__(self, num):
        self.num = num

    def addt0num(self, n):
        self.num = self.num + n

    @staticmethod   #Will help to ship that method with the class
    def add(a, b):
        return a+b


a = Math(5)
print(a.num)
a.addt0num(6)
print(a.num)

print(a.add(7, 2))
print(Math.add(7, 2))
