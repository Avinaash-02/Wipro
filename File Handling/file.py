# with open("virat_kohli.txt","a") as vt:
#     vt.write("He is also Known as the 'King Kohli'\n")
# with open("virat_kohli.txt","r") as vt:
#     data = vt.read()
#     print(data)
try:
    with open("msdhoni.txt","r")as msd:
        print(msd.read())
except FileNotFoundError:
    with open("msdhoni.txt","x") as msd:
        msd.write("Greatest player of all time")
    print("Hey file Does not exist")
