n = int(input("Enter the year: "))
if n%400==0 or (n%100!=0 and n%4==0) :
    print(f"Yes Year {n} is an leap year" )
else:
    print(f"No year {n} is not an leap Year ")
