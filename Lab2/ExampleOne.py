# This example shows us two things:
# First, that you can call a function within a for loop (very important!)
# and second, the syntax for iterating over a range of numbers in python.

# Notice how this function has no return statement, but a print statement?
# Python functions treat print statements as return statements if no other return
# statements exist in the function.
def count(num):
    print(num + 1)

if __name__ == "__main__":
    # This is pretty intuitive! All it does is iterate over the numbers
    # 1 to 10 and feeds them into our count function. You'll notice that
    # the computer knows to increment n by 1 for every pass of the loop.
    for n in range(10):
        count(n)