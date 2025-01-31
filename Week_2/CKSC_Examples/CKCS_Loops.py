# While loop section

user_input = str(input("Please enter a word: "))
user_list = []

# This may not run because our user might enter exit the first time he's prompted
while user_input.lower() != "exit":
	if user_input.lower() == "dog":
		print("Woof!")
	elif user_input.lower() == "cat":
		print("Meow!")
	user_list.append(user_input)
	user_input = str(input("Please enter another word (exit to stop): "))

# For Loop section
# We will use the user list

for item in user_list:
	# You can iterate over iterable items, even inside a for loop!
	#for letter in item:
	#	print(letter)
	print(f"Your string {item} is of length {len(item)}")

# If you want to use the indicies instead of the actual items inside an iterable object
for i in range(len(user_list)):
	print(f"Your string at index {i} is {user_list[i]}!")