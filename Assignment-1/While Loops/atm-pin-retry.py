correct_pin = "1928"
chance = 0
while chance <= 3:
    atm = input("Enter ATM Pin: ").strip()
    if atm==correct_pin:
        print("Successfully Logged in! ")
        break
    else:
        chance +=1
        print("Wrong pin")
if chance==3:
    print("Card Blocked")
