units = int(input("Enter total units consumed: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = (100 * 1) + (units - 100) * 2
else:
    bill = (100 * 1) + (100 * 2) + (units - 200) * 3

print("Your Electricity Bill is:", bill)
