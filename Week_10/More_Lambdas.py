'''
Here we look at lambdas! Don't be intimidated by their name
or syntax. They're just basic functions we define in-line. 
'''
if __name__ == "__main__":
	# We can assign it to a variable!
	add = lambda x, y: x + y
	print(add(2, 3))

	# Or we can use them in place like with the sorted function
	a_tuple_list = [(2, 3), (1, 5), (9, 0)]
	# Let's sort it by the second element
	# x is the argument, which is our inner element, and the index
	# is what we're sorting it by
	new_list = sorted(a_tuple_list, key=lambda x: x[1])
	print(new_list)