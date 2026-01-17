class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def display(self):
        return f'Name: {self.name}\n'f"Subject: {self.subject}"
teacher = Teacher("Avinaash","2312")
print(teacher.display())
