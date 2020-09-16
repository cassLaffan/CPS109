# Let's look at strings.
# Python likes to treat them like lists sometimes and their own datatype other times.
# For now, let's just say you want to cut up a string. Let's say you want to
# return a string without its first letter and several of its laster letters.
# It has, much like a list, indecies at each letter starting at 0.

# Let's assign our string to a variable first so we can manipulate it.
str = "This is a string!"

# Let's print it off to be sure.
print(str)

# Next, let's chop it up...
newStr = str[1:5]
# Let's note now that the first side of the [a:b] slide of a string is inclusive, so the h will be kept.
# However, the b part of the slide is not included. It is everything before index 5 in this case.

# Finally, let's print off our new string.
print(newStr)

# See what we did? We took a slice of the string at its indexes 1 to 5.
# To access a string or a list at a specific index, use square brackets.