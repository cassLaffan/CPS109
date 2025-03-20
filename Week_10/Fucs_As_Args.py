'''
This file shows how you can pass functions as arguments! Notice
that unlike in C++ where the functions pass in as arguments
will just be replaced with the values they return, functions
passed as arguments in Python can literally act as functions!
'''

def execute(func, value):
	# See? We're calling a function passed as an argument!
	x = func(value)
	return x

def square(x):
	return x * x

if __name__ == "__main__":
	print(execute(square, 5))