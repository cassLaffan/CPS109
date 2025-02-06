fruit_list = ["Strawberry", "Blueberry", "Grape", "Banana"]
x = 10

for number in range(x, 0, -1):
	print(number)

for index, fruit in enumerate(fruit_list):
	print(f"Index: {index}", f" Fruit: {fruit}")

new_list = [fruit.upper() for fruit in fruit_list]
print(new_list)

second_new_list = [num * 10 for num in range(10, -1, -1)]
print(second_new_list)