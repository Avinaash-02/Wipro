n = input("Enter String: ")
boolean = True
cnt=0
for i in n:
    if i in "aeiouAEIOU":
        cnt += 1
if cnt != 0:
    print(f'The count of Vowels in th String:{ cnt}')
else:
    print("No vowels Man!")
