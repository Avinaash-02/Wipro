with open('student_marks.txt', 'w') as infile:
    n = int(input("Enter the number of students: "))
    for i in range(n):
        name = input("Enter the name: ").strip()
        marks = int(input("Enter marks: "))
        infile.write(f"{name},{marks}\n")


def assign_grades(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 50 <= marks < 80:
        return 'C'
    elif 40 <= marks < 50:
        return 'D'
    else:
        return 'F'

with open('student_marks.txt', 'r') as infile, open('results.txt', 'w') as outfile:
    for line in infile:
        name, marks = line.strip().split(",")
        marks = int(marks)
        grade = assign_grades(marks)
        outfile.write(f"{name},{marks},{grade}\n")
