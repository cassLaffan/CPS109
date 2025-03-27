import os

if __name__ == "__main__":
	# Get the current working directory
	curr = os.getcwd()
	print(curr)

	# Change working directory
	os.chdir('/Users/courier/Documents')
	print(os.getcwd())
