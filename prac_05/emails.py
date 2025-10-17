"""
Estimated time: 25 minutes
Actual time: 30 minutes
"""

def main():
    """Collect user's email and name."""
    email_to_name = {}
    # Ask user to enter email
    email = input("Email: ")

    # Loop until user enters blank email
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").strip().upper()

        # If name isn't blank and user doesn't enter Y, ask for a correct name
        if name_confirmation != "" and name_confirmation != "Y":
            name = input("Name: ").title()

        # Store name and email in the dictionary
        email_to_name[email] = name
        email = input("Email: ")

    # Print results neatly
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract a name from the email."""
    # Get part before '@'
    prefix = email.split('@')[0]
    # Split at '.'
    parts = prefix.split('.')
    # Join and capitalise the first letter in the name
    name = " ".join(parts).title()
    return name

main()