if __name__ == "__main__":
	list_one = ['Banana', 'Orange', 'Kiwi', 'Jackfruit']
	list_two = ['Yellow', 'Orange', 'Brown', 'Brown?']
	# Last element gets chopped off
	list_three = [1.30, 2.50, 3.33, 10.10, 9.11]

	# Needs to be cast as a list in order to be printed in a meaningful fashion
	print(list(zip(list_one, list_two, list_three)))