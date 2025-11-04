"""
CP1404/CP5632 - Practical
More Guitars Exercise
"""

FILENAME = "guitars.csv"
from guitar import Guitar

def main():
    """Read guitars from CSV, display them, and sort by year."""
    guitars = load_guitars()
    print(f"{len(guitars)} guitars loaded from {FILENAME}.\n")

    display_guitars(guitars)

    # Sort by year and display
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


def load_guitars():
    """Load guitars from file."""
    guitars = []
    # Read guitars from file
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, year, cost = parts
                guitars.append(Guitar(name.strip(), int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display guitars in csv file."""
    # Display guitars
    print("My Guitars:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
