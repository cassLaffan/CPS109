# A demonstration of scopes

y = 20

def func():
	x = 10
	# Will cause the changes to y to persist after the function exits
	global y
	y = x + 5
	print(y)

func()
print(y)