'''
This is a demonstration of functions as class-first objects!
Note the syntax here. We don't use the () syntax for a function
in the main until we want to call the functionality!
'''

def greet():
	return "Hello, world!"

if __name__ == "__main__":
	# Assigning a function to a variable
	greet_func = greet
	# Calling the function through the variable
	print(greet_func()) 