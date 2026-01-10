n = input("Enter the string:").strip()
specific = input("Enter the specific character").strip()
cnt = 0
dic = {}
for i in n:
    dic[i] = dic.get(i,0)+1
print(dic[specific])
