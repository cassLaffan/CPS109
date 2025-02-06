if __name__ == "__main__":
	new_set = set()
	new_list = []
	user_input = input("Enter something! ")

	while user_input.lower() != "exit":
		new_list.append(user_input)
		new_set.add(user_input)
		user_input = input("Enter something! ")

	print(new_set)
	print(new_list)

	user_input = input("Enter something to remove: ")
	new_set.discard(user_input)
	print(new_set)
