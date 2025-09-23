MENU = """Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = calculate_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("> ").upper()
    print("Farewell!")


def print_stars(score: int):
    print("*" * score)


def calculate_result(score: float):
    """Return a message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_valid_score():
    score = int(input("Please enter a valid score: "))
    while score < 0 or score > 100:
        print("Invalid score! Must be 0–100.")
        score = int(input("Enter score (0–100): "))
    return score


main()
