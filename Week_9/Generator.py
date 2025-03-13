
def backwards_gen(lower, upper):
	num = upper
	while num != lower:
		yield num
		num = num - 1

if __name__ == "__main__":
	lower_input = int(input("Enter the lower limit of the range: "))
	upper_input = int(input("Enter the upper limit of the range: "))

	generated = backwards_gen(lower_input, upper_input)
	for num in generated:
		print(num)