'''
In this file, we're opening a file and reading it. We're not making 
any changes to the file!
'''
if __name__ == "__main__":
	# r is short for read
	# You can also take user input and open a file from the string they enter
	my_file = open("./A_File.txt", "r")

	# Reads everything from the file into string
	contents = my_file.read()
	content_list = contents.split("\n")
	print(content_list)
	for line in content_list:
		print(line)

	# We need to close the file!
	my_file.close()

	print("_____________________________")

	# We can also read the file line by line:
	filename = "./Halloween.txt"
	file = open(filename, "r")
	for line in file:
		print(line, end="")
	file.close()

	print("\n_____________________________")

	# We can also use the with block, which negates the requirement for the close func
	with open('./A_File.txt', 'r') as file:
		first_ten_chars = file.read(10)
		the_rest = file.read()
		print("The first 10 characters:", first_ten_chars)
		print("The rest of the file:", the_rest)

	print("_____________________________")

	# This block of code will do something similar to the split function above
	with open('./A_File.txt', 'r') as example_file:
		lines = example_file.readlines()
		print(lines)
	
	print("_____________________________")

	# Let's sort that list
	new_list = sorted(lines)
	print(new_list)