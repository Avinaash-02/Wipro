attendance=  list(map(int,input().split()))
val = 0
absent = 1
for i in attendance:
    if i!=0:
        val+=1
    else:
        absent+=1
print(f"Total Students {val}")
if absent:
    print(f"Total Absent : {absent}")
else:
    print(f"Total Absent: {'Nil'}")
