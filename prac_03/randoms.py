# What did you see on line 1?
# A random integer between 5 and 20, inclusive
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 5 and the largest number was 20

# What did you see on line 2?
# A random number chosen from 3, 5, 7, 9; starting at 3, counting upwards by 2 up to 10
# 10 is not included
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 3 and the largest number was 9

# What did you see on line 3?
# A random floating point number between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 2.5 and the largest number was 5.5

import random

print(random.uniform(1,100)) # for floating point numbers

print(random.randint(1,100)) # for integers

