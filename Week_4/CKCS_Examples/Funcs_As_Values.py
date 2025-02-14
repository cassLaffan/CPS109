
def prints_a_list(ls):
	print(*ls)

def does_stuff(function, a_list):
	function(a_list)

if __name__ == "__main__":
	variable = prints_a_list
	new_list = ["Banana", "Kiwi", "Mango", "Lemon", "Pear", "Strawberry"]
	variable(new_list)

	does_stuff(prints_a_list, new_list)