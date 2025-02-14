
def say_hello(a_name="Cassandra"):
	return f"Hello, {a_name}"

if __name__ == "__main__":
	print(say_hello("Tavis"))
	print(say_hello())

	new_list = ["Banana", "Kiwi", "Mango", "Lemon", "Pear"]
	
	print(*new_list)