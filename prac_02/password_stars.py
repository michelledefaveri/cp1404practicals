def main():
    minimum_length = 10

    password = get_password(minimum_length)

    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))


def get_password(minimum_length: int) -> str:
    password = input("Please enter a password:")
    while len(password) < minimum_length:
        print("Password is too short, try again")
        password = input("Please enter a password:")
    return password


main()
