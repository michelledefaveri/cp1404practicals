"""
CP1404 - Practical
Determine score status
"""

import random

def main():
    """ Get a user score, print the result, and generate a random score."""
    # Get user score
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)

    # Generate random score
    random_score = random.randint(0, 100)
    random_result = calculate_result(random_score)
    # Print result
    print(f"Random score: {random_score} \n{random_result}")


def calculate_result(score):
    """Return a message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

