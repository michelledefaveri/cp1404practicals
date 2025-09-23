

import random

Menu = "(G) Get valid name \n(A) Print asterisks \n(R) Print random number \n(Q) Quit"

def main():
    name = "user"
    print(Menu)
    choice = input("Enter your choice: ").upper()  # force uppercase
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "A":
            print_asterisks()
        elif choice == "R":
            print_random_number()
        else:
            print("Invalid Input. Try again")

        print(Menu)
        choice = input("Enter your choice: ").upper()

    print(f"Farewell {name}")

def get_valid_name():
    name = input("Enter your name: ")
    while name == "":
        print("Name can't be empty")
        name = input("Enter your name: ")
    return name

def print_asterisks():
    for i in range(1, 11):   # start at 1 to avoid printing empty line
        print("*" * i)

def print_random_number():
    random_number = random.randint(0, 100)
    print("Random number is", random_number)

main()












