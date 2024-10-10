class Employee:
    def __init__(self, department, role, salary):
        self.department = department
        self.role = role
        self.salary = salary
        
    def showDetails(self):
        print("Role: " + self.role + ", Department: " + self.department + ", Salary: " + self.salary)

        
e1 = Employee("IT", "emp", "25000")
e1.showDetails()

e2 = Employee("HR", "manager", "50000")
e2.showDetails()

e3 = Employee("Finance", "analyst", "45000")
e3.showDetails()
