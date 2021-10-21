def print_recursively(num):
    if num == 0:
        print("Starting to print at 0")
        return 0
    else:
        a = print_recursively(num - 1)
        print("Now we are at ", num)
        return num

if __name__ == "__main__":
    inp = int(input("What number of recursions would you like to see?"))
    print_recursively(inp)