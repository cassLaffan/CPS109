def find_element_in_list(required, ls):
	for item in ls:
		# the item we're looking for
		if item == required:
			print("Item found!")
			break
		else:
			print("Item isn't yet found!")
	else:
		# Logic that will only execute if the loop does not terminate early
		print("Item not found in list.")

def weather_report(weather):
	while weather.lower() == "snow":
		print("Stay inside and stay warm!")
		weather = str(input("What is the weather like now? "))
		if weather.lower() == "thunder":
			print("Take cover!")
			break
		else:
			print("Well at least it's not thundering!")

if __name__ == "__main__":
	lst = ['Banana', 'Orange', 'Kiwi', 'Jackfruit', 'Pineapple']
	find_element_in_list('Kiwi', lst)
	#weather_report("snow")
