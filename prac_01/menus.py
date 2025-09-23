"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name=input("Enter name:")

MENU= """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)

choice=input(">>>  ")

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid message")

    print(MENU)
    choice = input(">>>")
print("Finished")






