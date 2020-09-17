#Python primitive data type cheatsheet

#Note on Python and variable assignment: Python is a DYNAMICALLY TYPED language, 
# if you come from a Java background you will wonder why we aren't declaring any types during variable assignment.
#This is because in Python, variable types are evaluated at run time, meaning the program doesn't know the data type for
# it's variables until it executes the line where the variable gets assigned
# Also note: everything in Python is an 'objet' more on that later 

#Integers can be declared as numbers with no decimal point
#note when declaring a variable DO NOT USE RESERVED KEYWORDS this leads to confusion when reading your code
myInteger = 1

#floats (floating point numbers) can be declared as 
myFloating = 4.56789

#booleans (bools) can be declared similarly, but we won't do this often in code
myBool = True #note in python, True/False is always capitalized

#Strings can be declared with single quotes:
myString = 'This is a string'
#or with double quotes
myString2 = "This is a string"
#or with triple quotes spanning multiple lines
myString3 = '''This
is
a
string
'''
#or with triple double quotes spanning multiple lines
myString4 = """
This
is
a
string
"""

#note that we can get the type of a variable by using the 'type' function
#only used for debugging purposes
print(type(myInteger)) #<class 'int'>
print(type(myFloating)) #<class 'float'>
print(type(myBool)) #<class 'bool'>
print(type(myString)) #<class 'str'>

#Why does it say the word 'class' here? Because since everything in Python is an object, everything in the backend has what is called a 'Class definition'
#A class is used to define the properties,methods etc of an object
#An object is an 'instance' of a class
#more on that later in the course don't worry about this now...


#We can also cast objects and turn them into other objects ex:

intcast = int(myFloating) #transform float to integer, 'truncating' (removing) the fractional component (lose data)
floatcast = float(myInteger) #transforms integer to float
stringcast = str(myInteger) #transforms integer to string (note the 'print' function does this automatically)


#Integer Operations 
# Python supports: 
# the addition operator(+), 
# subtraction operator (-), 
# multiplication operator (*) 
# and division operator (/)
# Order of operations follows BEDMAS (Brackets, Exponents, Division, Multiplication, Addition, Subtraction)
##Bonus
# Integer division (removes fractions) (//)
# Modulus operator (%) returns only the remainder component from a division
# Exponent operator (**) e.g 2**4 = 16, 4**0.5 = 2
new_integer = (myInteger + 5) * 6 / 2 - 1 #What will the new_integer value be?
int_division = 7//2 #outputs 3
modulo = 3 % 2 #What will the modulo value be?
exp_example = 5**2
exp_example2 = 48**0.5 #Effectively taking the square root 

#All these operations also work on floats, but note that if you perform a division on an integer 
# that does not divide evenly the output will be a float to account for the decimal

#Boolean operations
#These can be useful for control statements
_integer = 10
mybool = True and False #False, both values need to be true in order to return true
mybool2 = True or False #True , one value needs to be true in order to return true
#the 'not' operator flips the boolean value from 'True' to 'False' and vice versa
mybool3 = not True #False
mybool4 = _integer == 10 #'==' is the equality operator, it checks if the values on either side are the same and evaluates to either true or false
mybool5 = _integer > 5 #True, Greater than sign checks if the value on the left is greater than the value on the right, can be used for floats, has many weird interactions with certain datatypes
mybool6 = _integer >= 10 #True This operator checks for both greater than, and equality
mybool7 = _integer < 5 #false
mybool8 = _integer <= 5 #false

#You can also group many operators together
# order of operations goes by Brackets > Everything else from left to right
question = False and True or False #what does this evaluate to?
question2 = (True or False) and True #what about this?
mega_bool = not(mybool3 and mybool4 or (not mybool5 and mybool6))
