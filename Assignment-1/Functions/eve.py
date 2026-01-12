def find_odd_even(val):
    return val%2==0
val = int(input("Enter the number to be checked: "))
if find_odd_even(val):
    print(f'The number {val} is Even')
else:
    print(f'The number {val} is Odd')
