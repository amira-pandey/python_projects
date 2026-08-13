# Inputs we need from the user
# Total rent
# Total food ordered
# Electricity units spent
# Charge per unit
# Persons living in the room/flat

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity units spent = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the room/flat = "))

# Calculate electricity bill
total_bill = electricity_spend * charge_per_unit

# Calculate amount each person has to pay
output = (food + rent + total_bill) / persons

print("Each person will pay =", output)
