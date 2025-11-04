
FILENAME = "guitars.csv"
from guitar import Guitar

def main():
    """Read guitars from CSV, display them, and sort by year."""
    guitars = []

    # Read guitars from file
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, year, cost = parts
                guitars.append(Guitar(name.strip(), int(year), float(cost)))

    print(f"{len(guitars)} guitars loaded from {FILENAME}.\n")

    # Display guitars
    print("My Guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort by year and display
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
