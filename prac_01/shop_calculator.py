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

"""
CP1404 - Practical
Get a password and print the length as asterisks
"""

def main():
    """ Get a password and print as asterisks. """
    minimum_length = 10
    password = get_password(minimum_length)
    print_asterisks(password)

def get_password(minimum_length):
    """ Prompt user to enter a valid password. """
    password = input("Please enter a password:")
    # Check password is greater than the minimum length
    while len(password) < minimum_length:
        print("Password is too short, try again")
        password = input("Please enter a password:")
    return password

def print_asterisks(password):
    """Print a line of asterisks equal to the length of the password. """
    # Print a line of asterisks equal to the password length
    print("*" * len(password))


main()
