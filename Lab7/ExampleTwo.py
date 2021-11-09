# This file will loop and write a line to a file so long as the user wants it to.
if __name__ == "__main__":

    our_file = open("yet_another_file.txt", "w") # w means you "write to it"

    inp = ""

    while inp != "Stop":
        inp = input("What would you like to write to the file?\n")
        if inp != "Stop":
            our_file.write(inp + "\n")

    our_file.close()