# a. Write code that asks the user for their name,
# opens a file called name.txt and writes that name to it.
out_file = open("name.txt","w")
name = input("What is your name?" )
print (name, file = out_file)
out_file.close()

# b. Write code that opens "name.txt" and reads the name then print "Hi {name}!"
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# c. Write code that opens numbers.txt, reads only the first two numbers,
# adds them together then prints the result
with open("numbers.txt","r") as in_file:
    number_one = int(in_file.readline())
    number_two = int(in_file.readline())
print(number_one + number_two)

# d. Print the total for all lines in numbers.txt.
total = 0
with open("numbers.txt","r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
