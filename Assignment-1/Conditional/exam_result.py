def grade_generator(val):
    if 90<=val<=100:
        return "A"
    elif 80<=val<90:
        return "B"
    elif 50<=val<80:
        return "C"
    elif 0 <= val <50:
        return "F"
marks = list(map(int,input("Enter the marks to know your Grade: ").split()))
for k in marks:
    j = grade_generator(k)
    print(j)
    if j=="A":
        print("Topper")
    elif j=="B":
        print("Average")
    elif j=="C":
        print("Satisfactory")
    elif  j=="F":
        print("Retry Dont worry ,God is with you. ")
