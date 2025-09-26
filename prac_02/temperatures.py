"""
CP1404 - Practical
Convert temperature between degrees and fahrenheit
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """ Display a menu to the user, get input, and perform temperature conversions. """
    print(MENU)
    # Get user choice
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def convert_fahrenheit_to_celsius(fahrenheit: float):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius: float):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


main()
