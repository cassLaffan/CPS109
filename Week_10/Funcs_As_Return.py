'''
Here, we can see that you can return a function instead of
a value in Python!
'''

def outer():
	def inner(a_value):
		return f"Hello from the inner function, {a_value}!"
	# Note that we can return the function by name?
	return inner

if __name__ == "__main__":
	# return_func stores the inner() function
	return_func = outer()
	# And we can call the returned function!
	print(return_func("wow!")) 
	var = return_func("Cass")
	print(var)