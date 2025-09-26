"""
CP1404 - Practical
Get a password and print the length as asterisks
"""

def main():
    """ Get a password and print as asterisks. """
    minimum_length = 10
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password: str):
    """Print a line of asterisks equal to the length of the password. """
    print("*" * len(password))


def get_password(minimum_length: int) -> str:
    """ Prompt user to enter a valid password. """
    password = input("Please enter a password:")
    # Check password is greater than the minimum length
    while len(password) < minimum_length:
        print("Password is too short, try again")
        password = input("Please enter a password:")
    return password


main()

