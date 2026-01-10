n = input("Enter String : ").strip()
up =""
lc =""
for i in n:
    up += i.upper()
for j in n:
    lc += j.lower()
print(f'Upper Case : {up}')
print(f'Lower Case : {lc}')
