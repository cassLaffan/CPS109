
if __name__ == "__main__":
	lst = ['Banana', 'Orange', 'Kiwi', 'Jackfruit', 'Pineapple', 'Strawberry']

	for fruit in lst:
		if len(fruit) % 3 == 0:
			print("Skipping this fruit!")
			continue
		print(fruit)