# Let's look at a for loop in a function!

# For loops can work anywhere in a program so long as they're correctly written
def for_loop_here(num):
    x = 1
    for i in range(num):
        print(i, " ", x)
        # x = x + i
        x+=i
    return x

if __name__ == "__main__":
    item = 5
    # Remember, you can skip extra lines by using the function and its argument(s)
    # as arguments for other functions, like print!
    # Also remember that you have to cast it to a string if you want to concatonate a string this way
    print("Our number is: " + str(for_loop_here(item)))