# This example is just to remind you guys how functions are called in Python. 
def backward_string(my_string):
    new_string = my_string[::-1]
    return new_string

# This shows a function that takes two arguments
def multiply_string(string_1, mulitplier):
    newer_string = string_1 * mulitplier
    return newer_string

if __name__ == "__main__":
    inp = "temp"

    while inp != "":
        inp = input("Enter a string to reverse:\n")
        if inp != "":
            i = int(input("How many times should it be repeated?\n"))
            print(backward_string(inp))
            print(multiply_string(inp, i))

    print("Good bye")