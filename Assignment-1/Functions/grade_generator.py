def grade_generator(val):
    if 90<=val:
        return "A grade"
    elif 80<=val<90:
        return "B grade"
    elif 50<=val<80:
        return "C grade"
    elif 0 <= val <50:
        return "Failed"
marks = int(input("Enter the marks to know your Grade: "))
print(grade_generator(marks))
