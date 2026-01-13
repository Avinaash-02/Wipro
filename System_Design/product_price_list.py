prices = list(map(float, input("Enter product prices: ").split()))
prices = [price * 1.10 for price in prices]
threshold = float(input("Enter minimum price to keep: "))
prices = [price for price in prices if price >= threshold]

print("Updated Prices:", prices)
