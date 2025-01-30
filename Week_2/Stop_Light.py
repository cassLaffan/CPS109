def light_switcher(user_input):
	print("Running the function!")
	if user_input.lower() == "red":
		print("Stop!")
	elif user_input.lower() == "yellow":
		print("Speed up!")
	elif user_input.lower() == "green":
		print("Go!")
	else:
		print("Your light is broken.")

if __name__ == "__main__":
	uinp = str(input("What colour is the light? Type 'exit' to get out of the car. "))
	while uinp.lower() != "exit":
		light_switcher(uinp)
		uinp = str(input("What colour is the light now? Type 'exit' to get out of the car. "))	