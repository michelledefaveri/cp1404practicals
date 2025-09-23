"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)

    # Generate random score at the bottom of main
    random_score = random.randint(0, 100)
    random_result = calculate_result(random_score)
    print(f"Random score: {random_score} \n {random_result}")


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


main()
