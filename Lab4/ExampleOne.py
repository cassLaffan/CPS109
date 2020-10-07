
def backward_string(my_string):
    new_string = my_string[::-1]

    return new_string



if __name__ == "__main__":
    
    inp = "temp"

    while(inp != ""):
        inp = input("Enter a string to reverse:\n")
        print(backward_string(inp))

    print("Good bye")