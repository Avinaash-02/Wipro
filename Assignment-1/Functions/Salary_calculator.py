def calc(lst):
    return sum(lst)
salary = list(map(int,input("Enter list of salaries: ").split()))
print(f'Total Value : {calc(salary)}')
