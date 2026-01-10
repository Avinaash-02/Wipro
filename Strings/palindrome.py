n = input("Enter String : ").strip()
def reverse(n):
    modified = ""
    for i in range(len(n)-1,-1,-1):
        modified += n[i]
    return modified

print(reverse(n),n)
if n==reverse(n):
    print(f"Given string '{n}'' is an palindrome")
else:
    print(f"Give String '{n}' is not a palindrome")
