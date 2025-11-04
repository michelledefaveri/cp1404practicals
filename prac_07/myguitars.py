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

    # Get user to enter new guitar details
    print("Enter new guitars.")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ").strip()

    # Save all guitars back to the file
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print(f"All guitars saved to {FILENAME}.")

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
