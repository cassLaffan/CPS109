# Basic function
def greeting():
	return "Hello!"

def call_twice(func):
	print(func())
	print(func())

def create_greeting():
	def a_greeting(arg):
		return f"This is a greeting, {arg}"
	return a_greeting

if __name__ == "__main__":
	# Assigning a function to a variable, thus 
	# creating a function object.
	var = greeting
	# Print the variable's location in memory
	print(var)
	# Invoking the function
	print(var())
	# Function as an argument for another function
	call_twice(var)
	call_twice(greeting)
	# Storing a returned function in a function object
	func_object = create_greeting()
	print(func_object("Cass"))