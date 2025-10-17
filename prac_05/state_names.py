"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

print(CODE_TO_NAME)

# Print all short states with their names aligned neatly
for code, name in CODE_TO_NAME.items():
    print (f"{code:3} is {name}")

# Ask user to enter a short state and return the appropriate name
state_code = input("Enter short state: ").upper()
# If blank, the program ends
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    # If invalid code is entered, ask user to re-enter
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()









