'''This is how you'd write the basic functionality shown in ExampleOne.py
correctly.'''

# Notice how I've abstracted some functionality out to a function
# Also, you'll notice how I've added a doc string inside the function
# definition before any functionality. This is the proper format
# for documenting your function. If you type help(print_list) into the
# console, it will print off the doc string description.
def print_list(ls):
    '''Takes a list and iterates through it, printing each element on a new line.'''
    for i in ls:
        print(i)

# Notice how the functionality not in the function is contained in the main!
# Notice how I have things named more meaningfully and not just their datatypes.
if __name__ == "__main__":
    my_list = input("Please enter a series of words seperated by spaces:\n").split()
    print_list(my_list)