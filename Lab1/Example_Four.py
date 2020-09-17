# Now here is a slightly more complex program that makes use of the boolean datatype
# and our ability to create our own functions

# Here we create a simple function in which we feed in a bool (True or False)
# and then return the opposite (the negated value of the True or False)
# Note that any variables assigned during a function call will be released/removed when the function exits
# This is due to the concept of SCOPE. Code written WITHIN a function (like in our example here) belongs to that
# function's SCOPE, meaning we cannot access the variable from outside the function
# note if we wanted to use a variable defined within a function, outisde of a function we can use the keyword 'global'
def get_value(value):
    return not value

# Finally, we call the function and print its value
print(get_value(False))
#print(value) #this does not work because we cannot access the 'value' paramater variable in the get_value function from this scope.

# Notice that we can pass the value of a function within the print function?
# We can pass functions in as arguments as python, so long as their datatypes match!