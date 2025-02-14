
# A function which returns a reversed string

def backward_string(a_string):
	# How to reverse a string quickly
	return a_string[::-1]

def muliply_string(new_string):
	return "The string " + new_string + " repeated 6 times is: " + (backward_string(new_string) * 6)

def inefficient_backwards_string(a_string):
	empty_string = ""

	for letter in range(len(a_string) - 1, -1, -1):
		empty_string = empty_string + a_string[letter]

	print(empty_string)

def this_function_doesnt_return_anything():
	pass

# This checks if this is the main module being run
if __name__ == "__main__":
	new_str = backward_string("Banana")
	print(new_str)
	print(muliply_string("Apple"))

	print(inefficient_backwards_string("Pear"))

	print(this_function_doesnt_return_anything())