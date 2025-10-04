"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user tries to enter a value which cannot be converted to an integer
such as a floating point number.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user enters the denominator as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""



valid_input = False

# While not loop so the program repeats until the user enters a valid input
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        # If user enters denominator as 0, ask them to try again
        if denominator == 0:
            print("Cannot divide by zero, try again.")
        else:
            fraction = numerator / denominator
            print(f"Result is {fraction:.2f}")
            valid_input = True

    # If ValueError is returned ask user to enter a valid input
    except ValueError:
        print("Numerator and denominator must be valid numbers, try again.")

print("Finished.")



