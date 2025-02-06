if __name__ == "__main__":
	new_dict = dict()
	user_input = input("Enter a key: ")
	while user_input.lower() != "exit":
		second_input = input("Enter a value: ")
		# Adds a key:value pair in the form of user_input : second_input
		new_dict[user_input] = second_input
		user_input = input("Enter a key: ")

	print(new_dict)

	for entry in new_dict:
		print(new_dict[entry])