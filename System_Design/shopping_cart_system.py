class Shoppingcart:
    def __init__(self):
        self.cart = []
    def add_item(self,product):
        self.cart.append(product)
    def remove(self,product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            return "Item is not in Cart"
    def show_cart(self):
        if self.cart:
            return self.cart
        return "Your cart is empty"
shop = Shoppingcart()
stop = 0
while stop == 0:
    print("Enter the products you want")
    product = input("products: ").strip()
    shop.add_item(product)
    stop = int(input("If you want to stop give 1: "))
    
print(shop.show_cart())
