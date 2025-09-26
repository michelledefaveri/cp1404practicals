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

