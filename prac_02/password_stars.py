def main():
    minimum_length = 10
    password = input("Please enter a password:")

    while len(password)< minimum_length:
        print("Password is too short, try again")
        password = input("Please enter a password:")

    print("*"*len(password))

main()
