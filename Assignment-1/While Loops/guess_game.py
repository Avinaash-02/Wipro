import random
value = int(input("Enter you number 1-10 (Lets try your luck):"))
if value == (random.randint(1,10)):
    print("Guessing Is blast Congrats : ",value)
else:
    print("So bad man !")
