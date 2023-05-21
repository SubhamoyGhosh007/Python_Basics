class Person:

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(self.name, self.occupation)


a = Person("Subhamoy", "Student")
a.info()
