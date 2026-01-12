products = list(map(int,input("Ener you products price list--> ").split()))
price = int(input("Enter you checking price: "))
print("Yes it is there" if price in products else " No it is not there Man!!!")
