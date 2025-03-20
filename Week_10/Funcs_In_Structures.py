'''
In this file, we explore how functions can be stored in iterable
data structures, such as lists.
'''
# Some basic functions
def add(a, b):
	return a + b

def multiply(a, b):
	return a * b

if __name__ == "__main__":
	# Storing the functions in a list
	operations = [add, multiply]
	# Calling the first function by index, giving it arguments
	print(operations[0](2, 3))
	var = operations[1](2, 6)
	print(var)