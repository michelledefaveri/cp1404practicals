"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

def main():
    """ Display a menu to the user, get input, and perform temperature conversions. """
    menu = """ C - Convert Celsius to Fahrenheit \n F - Convert Fahrenheit to Celsius \n Q - Quit"""
    print(menu)
    # Get user choice
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """ Convert fahrenheit to celsius. """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """ Convert celsius to fahrenheit. """
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()

