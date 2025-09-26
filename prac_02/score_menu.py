"""
CP1404 - Practical
Get a valid score, print the result, and show stars
"""

def main():
    """ Handle user input to get scores, print results, or show stars. """
    # Get an initial valid score from the user
    score = get_valid_score()
    menu = """ Menu: \n (G)et a valid score (0-100) \n (P)rint result \n (S)how stars \n (Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        # Get a new valid score
        if choice == "G":
            score = get_valid_score()
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

def get_valid_score():
    """ Prompt the user until they enter a valid score (0–100). """
    score = int(input("Please enter a valid score: "))
    # Check score is valid
    while score < 0 or score > 100:
        print("Invalid score! Must be 0–100.")
        score = int(input("Enter score (0–100): "))
    return score



main()
