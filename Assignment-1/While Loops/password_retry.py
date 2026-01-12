import time
correct_pin = "password"
chance = 0
while chance <= 3:
    password = input("Enter Password: ").strip()
    if password==correct_pin:
        print("Successfully Logged in! ")
        break
    else:
        chance +=1
        print("Wrong!")
if chance==3:
    print("try again after 10 seconds")
