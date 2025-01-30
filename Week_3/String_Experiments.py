a_string = "This is a string!"

split_string = a_string.split()
print(split_string)

print(a_string.lower())

# Get something at index -1
print(a_string[-1])

print(a_string[0])

print(a_string[4])

print("This is another string"[6])

# Important note: lower bound is inclusive,
# upper bound is exclusive
new_variable = a_string[0:4]
print(a_string[0:7])

variable_orange = " "
variable_apple = ""

print(variable_orange > variable_apple)