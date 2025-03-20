# A global variable (bad)
x = 20

def sum():
	# Doesn't work due to x becoming local
	# x = x + 30
	# Global tells Python to persist changes
	global x
	x = x + 30
	print(f"The value of local x is: {x}")

sum()
print(f"The value of global x is: {x}")