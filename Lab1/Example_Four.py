# Now here is a slightly more complex program that makes use of the boolean datatype
# and our ability to create our own functions

# Here we create a simple function in which we feed in a bool (True or False)
# and then return the opposite (the negated value of the True or False)
def get_value(value):
    return not value

# Finally, we call the function and print its value
print(get_value(False))

# Notice that we can pass the value of a function within the print function?
# We can pass functions in as arguments as python, so long as their datatypes match!