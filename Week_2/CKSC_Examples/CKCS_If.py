a = 10
b = 5
c = 2
# Conditional logic! Built off our boolean understanding
if a < b:
	print("Success!")
elif a % b == 0:
	print("Special success!")
elif a / b == 3:
	print("Another special statement!")
else:
	print("Not successful!")

# More complex conditions
# Or requires at least one of the conditions to be true
if (a == b) or (c != b):
	print("Complex condition one!")
# and requires both conditions on either side of it to be true
elif (c == b) and (c % 2 == 0):
	print("Complex condition two!")
# not flips true -> false and false -> true
elif not c == b:
	print("Not condition!")