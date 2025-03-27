'''
Try/except blocks allow you to create exception handling. You can deal
with errors, exceptions and generally funky behaviour!
'''

if __name__ == "__main__":
	# Basic try/except example
	try:
		# Attempt to convert user input to an integer
		number = int(input("Enter a number: "))
		print(f"You entered the number: {number}")

	except ValueError:
		# Handle the case where input is not a valid integer
		print("That's not a valid number! Please try again.")