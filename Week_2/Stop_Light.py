def light_switcher(user_input):
	print("Running the function!")
	if user_input == "red" or user_input == "Red":
		print("Stop!")
	elif user_input == "yellow" or user_input == "Yellow":
		print("Speed up!")
	elif user_input == "green" or user_input == "Green":
		print("Go!")
	else:
		print("Your light is broken.")

if __name__ == "__main__":
	uinp = str(input("What colour is the light? Please do not use all caps. "))
	light_switcher(uinp)
	uinp_two = str(input("What colour is the light now? Please do not use all caps. "))
	light_switcher(uinp_two)