n = input("Enter the String: ").strip()
ulta = ""
s = len(n)-1
while s >= 0:
    ulta+=(n[s])
    s-=1
print(ulta)
