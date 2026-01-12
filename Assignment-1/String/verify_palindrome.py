n= input("Enter the input: ").strip()
if n[::-1] == n:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
