n = input("Enter your password: ")
check = False
for i in n:
    if i in "!@#$%^&*()_+" or i in "1234567890":
        check = True
if check:
    print("Password is Strong: ")
else:
    print("Password is Weak")
