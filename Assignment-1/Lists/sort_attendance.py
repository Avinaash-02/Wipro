attendance = list(map(int,input("Enter your attendance: ").split()))
def bubble_sort(lst):
    Sorted = False
    while not Sorted:
        Sorted = True
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                Sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst
print(bubble_sort(attendance))
