def make_new_string(string):
    print("??"  + string + "!!")

if __name__ == "__main__":
    inp = ""
    # Notice how inp stays the same so the while loop can check it,
    # despite the fact that the function manipulates it?
    # Part of the reason is because the changes to inp are local only to the function.
    # The other part of the reason is strings are immutable, so these changes 
    # just create a new string, instead of editing the old one.
    while (inp != "end"):
        inp = str(input("Please enter a word:\n"))
        if (inp == "end"):
            break
        make_new_string(inp)