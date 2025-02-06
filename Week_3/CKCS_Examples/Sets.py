# Make an empty set
my_set = set()

user_input = str(input("Please enter a fruit: "))

while user_input.lower() != "exit":
	my_set.add(user_input)
	user_input = str(input("Please enter a fruit: "))

print(my_set)

user_input = str(input("Select an item to remove: "))

my_set.discard(user_input)

print(my_set)