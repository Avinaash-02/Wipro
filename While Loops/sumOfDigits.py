n = int(input("Enter the number: "))
sm = 0
while n!= 0:
    sm += n%10
    n//=10

print(f'Sum of digits: {sm}')
