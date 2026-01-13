attendance = list(map(int,input("Enter 1 - Present and 0 - Absent: ").split()))
print(f'Total Present: {attendance.count(1)}, Total Absent: {attendance.count(0)}')
