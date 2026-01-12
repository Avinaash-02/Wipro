age = int(input("Enter your age: "))
print("Do you have Lisense")
lisense = int(input("Choose 0 for No or 1 for Yes "))
if age >= 18 and lisense==1:
    print("You are eligible!")
elif age>=18 and not lisense:
    print("You are not eligible please take lisense")
else:
    print("You are not eligible ")
