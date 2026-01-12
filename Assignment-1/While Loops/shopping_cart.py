shopping_cart = []
for i in range(5):
    product = input("Enter the prodcut >")
    price = int(input("Enter the price >"))
    shopping_cart.append((product,price))
tot = 0
print(shopping_cart)
while i < len(shopping_cart):
    tot += shopping_cart[i][1]
    i+=1
print(f'total : {tot}')
