#Python primitive data type cheatsheet

#Note on Python and variable assignment: Python is a DYNAMICALLY TYPED language, 
# if you come from a Java background you will wonder why we aren't declaring any types during variable assignment.
#This is because in Python, variable types are evaluated at run time, meaning the program doesn't know the data type for
# it's variables until it executes the line where the variable gets assigned
# Also note: everything in Python is an 'objet' more on that later 

#Integers can be declared as numbers with no decimal point
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


#Integer Operations
new_integer = myInteger + 5 * 6 / 2 - 1