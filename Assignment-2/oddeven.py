numbers = list(map(int,input("Enter the set of numbers :").split()))
odd_cnt = 0
even_cnt = 0
for i in numbers:
    if i % 2== 0 :
        even_cnt += 1
    else:
        odd_cnt += 1
try:
    with open("Assignment-2/odd_even.txt", "w") as f:
        f.write(f"Odd count = {odd_cnt}\n")
        f.write(f"Even count = {even_cnt}\n")
except:
    pass
