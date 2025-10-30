"""
Estimated time = 30 minutes
Actual time = 24 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Store and display information about guitars entered by the user."""
    guitars = []
    print("My guitars!")
    # Get guitar details from user
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    # Add two predefined guitars
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Display the guitar list
    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            # Determine if the guitar is vintage
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars!")

if __name__ == "__main__":
    main()