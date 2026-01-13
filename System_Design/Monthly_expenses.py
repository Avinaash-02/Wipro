expenses = list(map(float, input("Enter monthly expenses: ").split()))

new_expense = float(input("Enter new expense: "))
expenses.append(new_expense)

total_expense = sum(expenses)
highest_expense = max(expenses)

print("Expenses List:", expenses)
print("Total Expense:", total_expense)
print("Highest Expense:", highest_expense)
