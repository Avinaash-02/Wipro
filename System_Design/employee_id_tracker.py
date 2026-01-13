class Employee:
    def __init__(self):
        self.employee_list = set()

    def check_status(self, data):
        if data in self.employee_list:
            return "Employee exists"
        else:
            return "No employee exists"

    def add_new(self, name, emp_id):
        employee = (name, emp_id)
        if employee in self.employee_list:
            print("Employee already exists")
        else:
            self.employee_list.add(employee)
            print("Employee added successfully")

    def display(self):
        return self.employee_list


emp = Employee()

while True:
    print("\nEnter the Employee Name and Id:")
    name = input("Enter the Name: ").strip()
    emp_id = int(input("Enter the employee Id: "))

    emp.add_new(name, emp_id)

    stop = int(input("If you want to stop the process: Press 1 "))
    if stop == 1:
        print("Thanks for updating .......")
        break

print("\nEmployee List:")
print(emp.display())
