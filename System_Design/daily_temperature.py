temperatures = [30, 32, 29, 35, 28, 31, 34]

average_temp = sum(temperatures) / len(temperatures)

above_average_days = []
for day, temp in enumerate(temperatures, start=1):
    if temp > average_temp:
        above_average_days.append((day, temp))

print(f"Average Temperature: {average_temp:.2f}°C")
print("Days with temperature above average:")
for day, temp in above_average_days:
    print(f"Day {day}: {temp}°C")
