class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} gets salary of RS. {self.salary}")


class Person(Employee):
    def showLog(self):
        print(f"Default subject of {self.name} : CS")


emp1 = Employee("Subhamoy" , 20000)
emp1.show()

emp2 = Person("Sonu", "30000")
emp2.show()
emp2.showLog()
