def get_expense(name, category):
    return float(input(f"Enter {category} expense: "))


print("===== Monthly Expense Analyzer =====")

name = input("Enter your name: ")

food = get_expense(name, "food")
rent = get_expense(name, "rent")
travel = get_expense(name, "travel")
other = get_expense(name, "other")

total = food + rent + travel + other
daily_avg = total / 30

print("\n----- Expense Report -----")
print(f"Name: {name}")
print(f"Total Expense: {total:.2f}")
print(f"Daily Average: {daily_avg:.2f}")
