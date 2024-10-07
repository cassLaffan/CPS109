if __name__ == "__main__":

    # Opens the file (in r mode)
    our_file = open("another_file.txt", "r")

    # Reads the file into the variable
    st = our_file.read()
    print("The file reads: ", st)

    # Closes the file
    our_file.close()