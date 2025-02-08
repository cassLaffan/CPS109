'''
This file just explores some of the functionalities we covered 
last week combined with list comprehensions!

List comprehension allows you to create a list based off another
iterable (such as a range, another list, etc.)
'''

if __name__ == "__main__":
	# We cannot escape the fruit list
	fruit_list = ["Strawberry", "Blueberry", "Grape", "Banana"]
	x = 10

	for number in range(x, 0, -1):
		print(number)

	for index, fruit in enumerate(fruit_list):
		print(f"Index: {index}", f" Fruit: {fruit}")

	# List Comprehensions require an expression that evaluates
	# then populates each element of your name list.
	new_list = [fruit.upper() for fruit in fruit_list]
	print(new_list)

	second_new_list = [num * 10 for num in range(10, -1, -1)]
	print(second_new_list)