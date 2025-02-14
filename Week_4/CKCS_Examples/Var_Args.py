
def unpacks_fruit(*fruits):
	for fruit in fruits:
		print(f"Unpacking {fruit} from grocery bag.")

if __name__ == "__main__":
	fruit_list = new_list = ["Banana", "Kiwi", "Mango", "Lemon", "Pear"]
	unpacks_fruit(*fruit_list)