"""
Estimated time: 25 minutes
Actual time: 30 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").strip().upper()

        if name_confirmation != "" and name_confirmation != "Y":
            name = input("Name: ").title()

        email_to_name[email] = name
        email = input("Email: ")

    # Print results neatly
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract a name from the email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()