variable_one = 1 # this is a variable that contains an int
print(variable_one)
print(4)

variable_two = 4.57 # this is a variable containing a float
print(variable_two)

variable_three = 'Hello!'
variable_four = "World!"
print(variable_three, variable_four)
print("This is a string!")

print(type(variable_four))
print(type(variable_one))

a, b, c = 2, 2.5, "two"
print(a, b, c)

cat_age, cat_name = 17, "Mischief"
print(cat_age, cat_name)

#---------- Math Operations Below -----------

print(2 + 4)
print(2 * 3)
# Power logic is base number times itself however many times the exponent is
# For example, 2 ** 3 == 2 * 2 * 2 -> 4 * 2 -> 8
print(2 ** 3)
print(3 ** 2) # 3 * 3 -> 9
# Modulo operator calculates the remainder!
print(8 % 3)
print(8 % 4)
# Note the difference in behaviour between the two divisions!
print(8/4)
print(8//4)

print(variable_one % variable_two)

# 8 + 10 / 5 -> 8 + 2 -> 10
var_a = int(8 + (12 - 2) / 5)
print(var_a)

var_a += 10
print(var_a)

# --------- User Input Examples -------------

'''
# This takes input from the user
user_input = str(input("Please input a string: "))
# F string, which allows you to format a string with other variable
print(f"Your string is {user_input}")

user_input += " likes cats!"
print(user_input)

user_input += str(variable_two)
print(user_input)
'''
# ------- Boolean logic -------

new_var = True
other_variable = 7 >= 2
print(other_variable)
print(other_variable == new_var)
print(variable_one != variable_two)
print(not (variable_one != variable_two))


print(new_var == other_variable and variable_one == variable_two)
print(new_var == other_variable or variable_one == variable_two)