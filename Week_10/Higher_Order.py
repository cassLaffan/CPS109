'''
In this file, I'll be demonstrating the usage of higher order functions.
'''

# Here again we see a function where the first argument is a function
def apply(func, value):
    return func(value)

if __name__ == "__main__":
    # Now, we call our function, where the function argument is a lambda!
	apply(lambda x: x ** 2, 4) 