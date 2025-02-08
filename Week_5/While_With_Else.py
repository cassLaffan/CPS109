'''
In this file, we're looking at a while loop with an else and a
continue statement.

An else after a loop will only execute of the loop does not exit
prematurely.

A continue statement will force a loop to its next iteration!
'''

if __name__ == "__main__":
	new_list = ["Banana", "Strawberry", "Kiwi", "Guava", "Mango", "Pineapple", "Watermelon"]
	count = -1
	while count < len(new_list) - 1:
		count+=1
		if count % 3 == 0:
			# This will force us to the next iteration of our while loop!
			continue
		print(f"The fruit at index {count} is {new_list[count]}")
	else:
		print("Finished the fruit while loop!")