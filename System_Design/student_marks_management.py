class Student:
    def __init__(self):
        self.tot = []
    def student_data(self,lst):
        self.lst = lst
        for i in lst:
            if lst[2] == 1:
                self.tot.append([lst[0],lst[1]])
    def result(self):
        if not self.tot:
            return "No active students Found !"
        l = sorted(self.tot , key = lambda x:x[1])
        return f'Maximum Marks By : Name: {l[-1][0]} Score : {l[-1][1]} Minimum Marks By : Name: {l[0][0]} Score : {l[0][1]}'
std = Student()
n = int(input("Enter Total number of students: "))
for i in range(n):
    name = input("Enter the Name of the Student: ").strip()
    marks = int(input("Enter the Student Marks: "))
    status = int(input("Enter 1(If student in school) or 0(If student is not in school) "))
    std.student_data([name,marks,status])
print(std.result())
