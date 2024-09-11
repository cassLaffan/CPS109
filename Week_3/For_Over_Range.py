if __name__ == "__main__":
    user_string = input("Please enter a string: ")

    # This program simply iterates through any given string.
    for i in range(len(user_string)):
        print(user_string[i] + "\t", end = "")