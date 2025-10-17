
COLOUR_TO_CODE = {
    "Aqua": "#00ffff",
    "Baby Blue": "#89cff0",
    "Brilliant Rose": "#ff55a3",
    "Cadmium Yellow": "#fff600",
    "Coquelicot": "#ff3800",
    "Corn": "#fbec5d",
    "Cornflower Blue": "#6495ed",
    "Cornsilk1": "#fff8dc",
    "Cotton Candy": "#ffbcd9",
    "French Mauve": "#d473d4"}

print(COLOUR_TO_CODE)

# Get user to enter a colour
colour_name = input("Enter a colour: ").title()
while colour_name != "":
    try:
        print(f"Colour code of {colour_name} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        # If colour not found, handle error
        print("Invalid colour name.")
    # Ask user to re-enter a colour name if invalid
    colour_name = input("Enter a colour: ").title()



