class Laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        return f'The laptop Brand: {self.brand} and  MRP: {self.price}'
# laptop = Laptop()
flag = 0
while not flag:
    brand = input("Enter your laptop brand: ").strip()
    price = int(input("Enter you Price: "))
    laptop = Laptop(brand,price)
    print(laptop.display())
    flag  = int(input("Choose 0 to continue or 1 to stop:"))
    if flag == 1:
        break
