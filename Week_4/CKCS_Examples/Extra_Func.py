from functools import reduce

def squares_a_number(num):
	return num**2

if __name__ == "__main__":
	lst = [10, 2, 3, 6, 100, -2]
	new_list = map(squares_a_number, lst)
	print(list(new_list))

	second_list = map(lambda x: x**3, lst)
	print(list(second_list))

	third_list = filter(lambda x: x % 2 == 0, lst)
	print(*list(third_list))

	# Ternery operation
	fourth_item = reduce(lambda a, b: a if (a > b) else b, lst)
	print(fourth_item)