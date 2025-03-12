'''
This file will demonstrate various kinds of scopes! Play around with
this file, and check where and when variables die.
'''

# y is global to this file and anything that imports it
y = 20

def foo():
	# x is local to foo
	x = 10
	print(x, y)

# If you have a global variable and need to modify it, 
# you can use the global keyword
def modify_global():
    global y
    y = 30


# Enclosing or nonlocal scope. Notice that the inner function
# can access the outer variable?
def outer():
	z = 10
	def inner():
		nonlocal z
		z = 20
	inner()
	print(z)  # 20



if __name__ == "__main__":
     outer()