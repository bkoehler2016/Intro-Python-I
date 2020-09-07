# For the exercise, look up the methods and functions that are available for use
# with Python lists.

import os
os.system("clear")

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(f'The answer should be [1,2,3,4] answer is {x}')

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(f'The answer should be [1,2,3,4,8,9,10] answer is {x}')

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
del x[4]
print(f'The answer should be [1,2,3,4,9.10] answer is {x}')

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5,99)
print(f'The answer should be [1,2,3,4,9,99,10] answer is {x}')

# Print the length of list x
# YOUR CODE HERE
len(f'The length of x is {x}')

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
new_x = [ i *1000 for i in x]
print(f'This is every value in the list multipled by 1000 {new_x}')