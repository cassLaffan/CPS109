# This file shows us if statements and the steps you might need for them.
# There are three potential steps in an if statment (you don't always need all three)

# This function will just compare its two arguments, x and y.
def if_bigger(x, y):
    # If you have a logical set of checks that flow naturally from one another,
    # first you start with "if". This one is always necessary because it tells the computer
    # that any other checks following it are only if the first condition isn't met.
    if (x < y):
        print("X is bigger than Y.")
    # Elif is short for "else if". This indicates to the computer that if the previous condition
    # isn't met, that this one should be checked next. This one isn't really necessary, but good practice.
    elif (y > x):
        print("Y is bigger than X.")
    # Else tells the computer that if none of the preceeding conditions are met, that it has
    # to execute this one.
    else:
        print("X and Y are equal.")
