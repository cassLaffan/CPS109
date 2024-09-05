# A short example converting to binary strings
# Why?

# ¯\_(ツ)_/¯

if __name__ == "__main__":
    
    my_input = 0

    while my_input != -1:
        my_input = int(input("Enter a number you want to see in binary!\n"))
        if my_input >= 0:
            # The bin function gives us the binary representation of positive
            # integers in Python.
            print(bin(my_input))
        else:
            print("This should be done in C.") # Ask me why lol
            # Hint: Python doesn't have much of a notion of signed vs. unsigned ints.

    print("Goodbye!")