temperature = int(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing !")
elif temperature <= 25:
    print("Normal Temperature")
elif temperature <= 40:
    print("Hot Weather !")
else:
    print("Extreme Heat !")
