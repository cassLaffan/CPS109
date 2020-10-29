if __name__ == "__main__":

    our_file = open("a_file.txt", "r") # r means you "read from it

    st = our_file.read(250) # Notice we include how many characters we want to read in?
    print("The file reads: ", st)

    our_file.close()