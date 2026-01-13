feedback = input("Enter your valuable Feeback: ").strip()
q = 0
for i in feedback:
    if i in "aeiouAEIOU":
        q+=1
print(f"The count of vowels in feedback is {q}")
