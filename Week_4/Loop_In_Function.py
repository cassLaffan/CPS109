# Let's look at a for loop in a function!

# For loops can work anywhere in a program so long as they're correctly written
def for_loop_here(num):
    x = 1
    for i in range(num):
        # x = x + i
        x+=i
        print("x is now: ", x)
    return x

if __name__ == "__main__":
    item = 5
    # Remember, you can skip extra lines by using the function and its argument(s)
    # as arguments for other functions, like print!
    # Also remember that you have to cast it to a string if you want to concatonate a string this way
    a = for_loop_here(item)
    print("Our number is: " + str(a))