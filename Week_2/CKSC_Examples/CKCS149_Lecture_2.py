var_one = 11
var_two = 12

print(f"The value of these variables are {var_one} and {var_two}")

var_three = "Hello, world!"
var_four = var_three.lower() # Makes all the letters lower
var_five = var_three.upper() # Makes all the letter upper case!

print(f"Our strings are {var_four} and {var_five}")
print(var_three)

print(var_three[0])
print(var_three[-1])
print(var_three[3])

sliced_variable = var_five[2:10]
print(sliced_variable)

str_one = "apple"
str_two = "anana"

print(str_one > str_two)

new_str = str_two.split("a")
print(new_str)