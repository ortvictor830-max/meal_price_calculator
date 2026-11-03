#I have added a tip rate calculator to the meal cost calculator and displayed the tip amount.
#I have asked the user to input a tip rate instead of a tip amount. 
price_child_meal = float(input("What is the price of a child's meal? "))
price_adult_meal = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))    
print()
#calculate total cost of meals
total_cost = (price_child_meal * number_of_children) + (price_adult_meal * number_of_adults)
print(f"Subtotal: ${total_cost:.2f}")
print()
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = total_cost * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")
tip_rate = float(input("What is the tip rate? ")) / 100
tip_awarded = total_cost * tip_rate 
print(f"Tip: ${tip_awarded:.2f}")
total_meal_price = total_cost + sales_tax + tip_awarded
print(f"Total: ${total_meal_price:.2f}")
print() 
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_meal_price
print(f"Change: ${change:.2f}")
