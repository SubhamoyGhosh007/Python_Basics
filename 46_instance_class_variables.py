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

emp1 = Employee("Me")
print(f"Employee Number : {Employee.noOfEmployee}")  #1
emp1.rase_amount = 0.3
emp1.company_name = "Samsung"
# emp1.showDetails()
Employee.showDetails(emp1)  #same as above

emp2 = Employee("Sonu")
emp2.showDetails()


Employee.company_name = "Google"
emp2.showDetails()

# Employee.name = ".." Error

print(f"Employee Number : {Employee.noOfEmployee}")  #2
emp3 = Employee("Subhamoy")
print(f"Employee Number : {Employee.noOfEmployee}")  #3
