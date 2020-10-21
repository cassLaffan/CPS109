# Let's write a very basic recursive function.
# Remember, a recursive function is just a function that calls itself
# somewhere in its code.

# This function will do one of two things
# If num is odd, it will recursively call itself on the next lowest number.
# If the number is even, it will return a new number which is num * 2
def our_recursion(num):
    new_num = 0

    if(num % 2 != 0):
        new_num = our_recursion(num - 1)
    else:
        new_num = num * 2

    return new_num


if __name__ == "__main__":

    rec_call = our_recursion(3)
    print(rec_call)
