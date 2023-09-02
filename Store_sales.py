# Product data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products
total_price_average = sum(prices) / len(prices)

# Create a new price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]

# Calculate the total revenue generated from the products
total_revenue = sum(prices[i] * last_week[i] for i in range(len(prices)))

# Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / sum(last_week)

# Find products with prices less than $30 based on the new prices
products_less_than_30 = [products[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Output the results
print("Total Price Average:", total_price_average)
print("New Prices:", new_prices)
print("Total Revenue:", total_revenue)
print("Average Daily Revenue:", average_daily_revenue)
print("Products with Prices Less Than $30:", products_less_than_30)