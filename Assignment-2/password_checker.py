n = int(input("Enter the Number of Passwords: "))
def chk(val):
    spl = 0
    length = 0
    digits = 0
    for i,k in enumerate(val):
        if k in "!@#$%^&*()_+}{:?><.,/":
            spl += 1
        elif k in "0987654321":
            digits += 1
        length += 1
    return [spl,digits,length]
lst = []
for i in range(n):
    verdict = False
    s = input("Enter the Password: ").strip()
    spl,digits , length = chk(s)
    if spl!=0 and digits!=0 and length>=8:
        verdict = True
    lst.append(f"Password:{ s}, special_numbers - {spl if spl!=0 else 0}, Digits - {digits if digits != 0 else 0}, length - {length if length!= 0 else 0},Verdict : {'Strong' if verdict else 'weak'}")
try:
    with open("Assignment-2/Passwords_list.txt","a") as fl:
        for i in lst:
            fl.write(i+"\n")
except:
    pass
