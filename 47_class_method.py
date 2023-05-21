class Employee:
    company_name = "Apple" #class variable
    noOfEmployee = 0
    def __init__(self,name):
        self.name = name
        self.rase_amount = 0.02  #instance variable
        Employee.noOfEmployee += 1
    def showDetails(self):
        print(f"Name is : {self.name}")
        print(f"Raise Amount is : {self.rase_amount}")
        print(f"Company Name is : {self.company_name}")

    @classmethod
    def changeCompany(cls, newCompany):  #first parameter is for self without @classmethod
        cls.company_name = newCompany

e1 = Employee("Subhamoy")
e1.showDetails()
e1.changeCompany("Tesla")

print(Employee.company_name)