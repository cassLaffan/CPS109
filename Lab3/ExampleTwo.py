# Now let's iterate through a string instead.

if __name__ == "__main__":
    user_string = input("Please enter a string: ")

    # This program simply iterates through any given string.
    for i in range(len(user_string)):
        print("Current index: ", i)
        print(user_string[i], end=" ")