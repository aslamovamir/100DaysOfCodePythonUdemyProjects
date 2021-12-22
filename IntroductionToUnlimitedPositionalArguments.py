# Introduction to Unlimited Positional Arguments

# modify the add function to take an unlimited number of arguments
# use a loop to sum all the arguments inside the function

# the type of the args passed is a tuple
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(9,19,20,100,23))
