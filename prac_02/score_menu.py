"""
CP1404 - Practical
Get a valid score, print the result, and show stars.
"""

MENU = """Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    """ Handle user input to get scores, print results, or show stars. """
    # Get an initial valid score from the user
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        # Get a new valid score
        if choice == "G":
            score = get_valid_score()
        # Print the result of the current score
        elif choice == "P":
            result = calculate_result(score)
            print(result)
        # Print stars equal to the score
        elif choice == "S":
            print_stars(score)
        # Invalid menu option
        else:
            print("Invalid option")
        print(MENU)
        choice = input("> ").upper()
    print("Farewell!")


def get_valid_score():
    """ Prompt the user until they enter a valid score (0–100). """
    score = int(input("Please enter a valid score: "))
    # Check score is valid
    while score < 0 or score > 100:
        print("Invalid score! Must be 0–100.")
        score = int(input("Enter score (0–100): "))
    return score

def calculate_result(score: int):
    """ Return a message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score: int):
    """ Print a line of stars equal to the score. """
    print("*" * score)


main()
