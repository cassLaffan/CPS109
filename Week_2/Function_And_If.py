# This file shows us if statements and the steps you might need for them.
# There are three potential steps in an if statment (you don't always need all three)

# This function will just compare its two arguments, x and y.
def if_bigger(x, y):
    if (x > y):
        print("X is bigger than Y.")
    # Elif is short for "else if". This indicates to the computer that if the previous condition
    # isn't met, that this one should be checked next. This one isn't really necessary, but good practice.
    elif (y > x):
        print("Y is bigger than X.")
    # Else tells the computer that if none of the preceeding conditions are met, that it has
    # to execute this one.
    else:
        print("X and Y are equal.")
    
    return x

if __name__ == "__main__":
    if_bigger(5, 7)
    i = if_bigger(5, 3)
    if_bigger(4, 4)
    print(i)