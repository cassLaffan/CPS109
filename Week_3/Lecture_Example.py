def string_list_func(lst):
	# Getting the length of our list
	lst_len = len(lst)
	count = 0

	while count < lst_len:
		print(lst[count])
		count+=1

if __name__ == "__main__":
	user_input = str(input("Enter a word that isn't 'end': "))
	user_list = []

	while user_input.lower() != "end":
		user_list.append(user_input)
		user_input = str(input("Enter a word, it can be 'end': "))

	string_list_func(user_list)

	print("Goodbye!")
