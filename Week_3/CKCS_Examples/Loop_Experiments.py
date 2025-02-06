new_list = ["Banana", "Strawberry", "Kiwi", "Guava", "Mango", "Pineapple", "Watermelon"]

for fruit in new_list:
	print(fruit)
	if fruit == "Mango":
		pass
	else:
		print("This fruit is not a mango.")
	print("But it is a fruit!")	
else:
	# Loop else statements are mutually exclusive to break statements
	# if a break statement is met, the else statement won't evaluate!
	print("Found the mango!")


for fruit in new_list:
	for letter in fruit:
		if letter == "i":
			break
		print(letter, end=" ")
	else:
		print("\nThis fruit doesn't have an i in it!")
	print() # prints a new line

count = -1
# Since I am incrementing count first, we needed to start at -1, and then increment from there
# However, since the check on line 26 is prior to incrementation, we risk an index out of
# range error. Thus, we change the bound such that it doesn't happen!
while count < len(new_list) - 1:
	count+=1
	if count % 3 == 0:
		continue
	print(f"The fruit at index {count} is {new_list[count]}")
else:
	print("Finished the fruit while loop!")
