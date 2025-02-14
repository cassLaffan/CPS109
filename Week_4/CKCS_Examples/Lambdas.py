
if __name__ == "__main__":
	# This variable will store this functionality for later
	adds_four = lambda a, b, c, d: a + b + c + d
	print("Hi!")
	print(adds_four(2, 4, 2, 7))
	print(adds_four(10, 20, 30, 10))
	# We killed the function and can't access it anymore on line 9 onwards
	adds_four = 20
	print(adds_four)

	new_list = ["Banana", "Kiwi", "Mango", "Lemon", "Pear"]
	# Try sorting this list without using the lambda
	new_list.sort(key=lambda x: x[1])
