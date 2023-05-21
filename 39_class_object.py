class Person:
    name = "Subhamoy"
    occupation = "Student"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
print(a.name)

a.name = "Sonu"
print(a.name,a.occupation)
a.info()

b = Person()
b.info()