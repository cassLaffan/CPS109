# Let's do an example of a loop that relies on the user entering a specific
# input for it to terminate. In this case, so long as the user doesn't 
# enter 1, it will loop forever.

if __name__ == "__main__":
    x = -1

    while x != 1:
        # You'll notice that we don't take into account the user
        # being a jerk and entering something that isn't a number.
        # Don't worry, we'll get to that later.
        x = int(input("Please enter a number:\n"))
    print("Thank you!")
