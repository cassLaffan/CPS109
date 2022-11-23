'''Here is our first example of what a BAD program looks like'''

# First problem: we have a variable named after its data type
# Stop doing this. This is not only bad practice but will often 
# times lead to unpredictable behaviour. Not only that, other
# languages simply don't allow it.

# Second problem: list and the succeeding for-loop are sitting in
# the ether.
list = input("Enter a bunch of words seperated by spaces.").split()

for i in list:
    print(i)

# Not only are the list and for-loop sitting in the ether, the main is
# sitting here and doing nothing. We use the main for a reason!
if __name__ == "__main__":
    pass