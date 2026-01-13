lst = list(map(int,input("Enter the list of numbers: ").split()))
cnt = 0
for i in lst:
    if i%2==0:
        cnt +=1
print(cnt)
