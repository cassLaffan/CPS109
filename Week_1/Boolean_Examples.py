# One more example. Let's deal with OR and AND

# These just check the true status of whatever is on either side of the operator.

print(True and False) # Will return False because the second condition is false!

print(not(True) and True) # Will return False because of the negation.

# You can assign these to variables like any other datatype.
x = False
y = True

# Do you know what this will print off?
print((x and y) or (y and y))

# You can, in principle, string as many of these together as your heart desires.

print(x or y and y or x) # Hehe you just have to keep your logic in check. I would reccomend using brackets.