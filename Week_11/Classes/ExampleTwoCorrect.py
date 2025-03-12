'''Here is how you would write the functionality in ExampleTwo.py
correctly.'''

# You will notice how, again, I have a doc string after the
# declaration.
def print_these_strings(str_one, str_two):
    '''Takes two strings and prints them sequentially.'''
    print(str_one)
    print(str_two)

# Notice how I keep variables local.
if __name__ == "__main__":
    a = input("Please input your first string:\n")
    b = input("Please input your second string:\n")
    print_these_strings(a, b)