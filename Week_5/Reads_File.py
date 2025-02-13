
if __name__ == "__main__":
	our_file = open("./Season_Of_The_Witch.txt", "r")
	
	line_string = our_file.readline()
	counter = 1

	while line_string:
		if counter == 5:
			print("\t", line_string, end="")
			counter = 1
		else:
			print(line_string, end="")
			counter+=1
		line_string = our_file.readline()

	our_file.close()