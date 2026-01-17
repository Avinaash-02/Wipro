class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
name = input("Enter the name: ").strip()
roll_number = int(input("Enter the Roll number: "))
std = Student(name, roll_number)
print(f"The Stdudent Name: {std.name}")
print(f"The Roll Number: {std.roll_number}")
