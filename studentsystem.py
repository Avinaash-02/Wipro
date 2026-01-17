class Student:
    def __init__(self,name,student_id,marks):
        self.test_for = 600
        self.name = name
        self.student_id = student_id
        self.marks = marks
        self.tot = sum(self.marks)
        self.avg = self.tot//len(marks)
    def calculate_grade(self):
        percentage = (self.tot / self.test_for) * 100
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "Fail"

    def calculate_status(self):
        self.grade = self.calculate_grade()
        if self.grade == "A":
            return "Extraordinary"
        elif self.grade =="B":
            return "Excellent"
        elif self.grade == "C":
            return "Good"
        elif self.grade =="D":
            return "Try better"
        else:
            return "Failed, Please son imporve next time!!!"
with open("students_data.txt","a") as fl:
    n = int(input("Enter the number of student Entries: "))
    for i in range(n):
        name = input("Enter the Student Names: ")
        marks = list(map(int,input("Enter the marks For 6 Subject: ").split()))
        roll = int(input("Enter the roll number: "))
        fl.write(f"{name},{roll},{','.join(map(str,marks))}\n")
try:
    with open('students_data.txt','r') as fl:
        # name,student,marks=fl
        for i in fl:
            parts = i.strip().split(",")
            name = parts[0]
            roll = parts[1]
            marks = list(map(int,parts[2:]))
            total = sum(marks)
            student =Student(name,roll,marks)
            print("-"*30)
            print(f'Student Name: {name}')
            print(f'Roll No: {roll}')
            print(f'Total Marks Scored: {total}')
            print("Grade: ",student.calculate_grade())
            print("Status: ",student.calculate_status())
            print("-"*30)

except Exception as e:
    print("Exception: ",e)
