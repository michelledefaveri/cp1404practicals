"""
CP1404 - Practical
Get a valid score, print the result, and show stars
"""

def main():
    """ Handle user input to get scores, print results, or show stars. """
    # Get an initial valid score from the user

    menu = """ Menu: \n (G)et a valid score (0-100) \n (P)rint result \n (S)how stars \n (Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        # Get a new valid score
        if choice == "G":
        # Get valid score
        # Print the result of the current score
        elif choice == "P":
        # Calculate result
        # Print stars equal to the score
        elif choice == "S":
        # Print stars
        # Invalid menu option
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell!")


main()
