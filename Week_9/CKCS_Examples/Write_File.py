'''
Here, we're going to open a file in write mode and write content to it.
'''
if __name__ == "__main__":
	# The w stands for write
	# It will create a file if it doesn't exist!
	with open('topics.txt', 'w') as output_file:
		output_file.write("Computer Science")
	
	# a is for append, which will tack stuff onto the end of a file!
	with open('topics.txt', 'a') as output_file:
		output_file.write(" is rewarding!")

	with open('topics.txt', 'r') as output_file:
		contents = output_file.read()
		print(contents)
	