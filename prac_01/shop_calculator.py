"""
Get number of items
Check for invalid inputs and get user to re-enter the number of items if invalid
Get user to enter the price of each item
Get total price
Take discount if the total price is over $100
"""

number_of_items = int(input("Number of items:"))

if number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items:"))

total_price=0
for i in range(number_of_items):
    price= float(input("Price of item:"))
    total_price= total_price + price

if total_price > 100:
    total_price = total_price * 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")



