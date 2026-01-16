n = list(map(int,input("Enter the numbers: ").split()))
# file_read = open('number_input.txt','r')
file_write = open('prime_number_output.txt','w')
def prime(n):
    if n<=1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True
ans = []
for i in n:
    if prime(i):
        ans.append(i)
file_write.write(str(f"Prime numbers are: {ans}"))
# print(i)
