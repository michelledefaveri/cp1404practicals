import random

low = int(input("Enter low value:"))
high = int(input("Enter high value:"))

while high<=low:
    print("Not valid. Make sure high value is greater than low:")
    high = int(input("Enter high value:"))

n=random.randint(low,high)
print(":)"*n)





