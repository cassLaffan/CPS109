'''
Break statements will stop a loop in its tracks. Furthermore,
if you have an inner and an outer loop, a break in the inner
loop will only stop the inner loop!
'''

if __name__ == "__main__":
	new_list = ["Banana", "Strawberry", "Kiwi", "Guava", "Mango", "Pineapple", "Watermelon"]

	for fruit in new_list:
		for letter in fruit:
			# This will only break us out of this inner loop
			if letter == "i":
				break
			print(letter, end=" ")
		else:
			print("\nThis fruit doesn't have an i in it!")
		print() # prints a new line