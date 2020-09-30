# Now let's iterate through a string instead.

if __name__ == "__main__":
    user_string = input("Please enter a string: ")

    # This program simply iterates through any given string.
    for i in user_string:
        print(i + " ", end = "")