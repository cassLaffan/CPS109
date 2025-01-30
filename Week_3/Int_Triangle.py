def int_triangle(num):
	count = 1
	while count <= num:
		inner = 1 # Counter for inner loop
		while inner <= count:
			print(inner, end=" ")
			inner+=1
		print()
		count+=1

if __name__ == "__main__":
	inp = int(input("Please enter a number. "))
	int_triangle(inp)