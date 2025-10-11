import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    """Get number of quick picks and print result."""
    number_of_quick_picks = get_number_of_quick_picks()
    quick_picks = generate_quick_picks(number_of_quick_picks)
    for quick_pick in quick_picks:
        print_quick_picks(quick_pick)


def get_number_of_quick_picks():
    """Get valid number of quick picks."""
    # Ask user for input and ensure it’s not negative
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Please try again")
        number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks


def generate_quick_picks(number_of_quick_picks):
    """Generate the requested number of quick picks."""
    # List to store all quick picks (rows)
    quick_picks = []
    # Generate one quick pick per loop
    for i in range(number_of_quick_picks):
        quick_pick = []
        # Generate random numbers for each line
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            # Avoid repetition
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        # Sort the numbers into ascending order
        quick_pick.sort()
        # Add this quick pick (row) to the list of all picks
        quick_picks.append(quick_pick)
    return quick_picks


def print_quick_picks(quick_pick):
    """Print quick pick nicely formatted."""
    print(" ".join(f"{number:2}" for number in quick_pick))


main()

