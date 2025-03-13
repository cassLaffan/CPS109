def fibonacci(n):
	# Base cases
	if n == 0:
		return 0
	elif n == 1:
		return 1
	# Recursive case
	else:
		print(f"Recursive call, n = {n}!")
		return fibonacci(n - 1) + fibonacci(n - 2)
	
if __name__ == "__main__":
	print(fibonacci(8))