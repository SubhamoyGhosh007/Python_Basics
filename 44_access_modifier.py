class Employee:
    def __init__(self):
        self.name = "Me"  #Public
        self.__name = "Sonu"  #Private   | Weak internal use indicator


a = Employee()
print(a.name)
# print(a.__name) Error
print(a._Employee__name)  #name mangling => obj._class__attribute
print(a.__dir__())