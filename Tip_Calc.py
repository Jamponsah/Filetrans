# Charge for food from the user
food_charge = float(input("Enter the charge for food: $"))

# Tip (18%)
tip = 0.18 * food_charge

# Sales tax (7%)
sales_tax = 0.07 * food_charge

# Grand total
grand_total = food_charge + tip + sales_tax

# Results
print(f"Tip = ${tip:.2f}")
print(f"Sales tax = ${sales_tax:.2f}")
print(f"Grand total = ${grand_total:.2f}")