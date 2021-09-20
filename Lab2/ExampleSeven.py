# This example goes over how to use lists and
# strings for loops.

# So here we have a definition of a function that takes
# a string as an argument. Then, it iterates over the 
# contents of the string and prints out the characters one 
# at a time.
def loop_over_string(my_string):

    # Notice that I have range(len(my_string))
    # Why? Well, this is how you iterate over a collection of numbers
    # in a specific range. It begins at the first number inclusive
    # and then ends at the last number NOT inclusive.
    for c in range(len(my_string)):
        print(my_string[c])

# Here I have defined a function that takes a list as an argument
# Then it iterates over each item in the list, just like in the string above
def loop_over_list(my_list):
    for i in range(len(my_list)):
        # The square brackets are the syntax for finding an item in a list (or string)
        # given the index number.
        print(my_list[i])

if __name__ == "__main__":
    # Recall: a string is just something contained in quotations
    this_string = "This is our string"

    # This is a list of strings. A list is denoted by square brackets on either side
    # and its contents are seperated with commas
    this_list = ["this", "is", "our", "list"]

    # Now we call the functions
    loop_over_string(this_string)
    loop_over_list(this_list)