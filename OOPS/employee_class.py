class Employee:
    emp_data = {}
    def __init__(self,name,salary):
        self.name = name
        self.salary= salary
        Employee.emp_data[self.name] = self.salary
    @classmethod
    def result(cls):
        for i,j in cls.emp_data.items():
            print(f"The Employee Name: {i} Salary: {j}")
n = int(input("Enter the number of Employee: "))
# emp = Employee()

for i in range(n):
    name = input("Enter the Name: ").strip()
    salary = int(input("Enter the salary of the employee: "))
    Employee(name ,salary)
Employee.result()
