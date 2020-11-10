# This example is just to remind you guys how functions are called in Python. 
# Except there's a twist! Notice those crazu equals and their values?
def backward_string(my_string="Heck"):
    new_string = my_string[::-1]
    return new_string

# This shows a function that takes two arguments
def multiply_string(my_string, mulitplier=1):
    newer_string = my_string * mulitplier
    return newer_string

if __name__ == "__main__":
    
    inp = "temp"

    while(inp != "Stop"):
        inp = input("Enter a string to reverse:\n")
        if(inp != ""):
            i = int(input("How many times should it be repeated?\n"))
            print(backward_string(inp))
            print(multiply_string(inp, i))
        else:
            print("How many times should the default be repeated?\n")
            print("Wait I don't care!\n")
            new_string = backward_string()
            print(new_string)
            print(multiply_string(new_string))

    print("Good bye")