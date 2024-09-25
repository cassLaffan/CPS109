# Assume the user_input is an integer
def right_triangle(user_input):
    iterator = 1
    while iterator <= user_input:
        second_itr = 1
        while second_itr <= iterator:
            print(second_itr, end=" ") # Overrides the end of a line with a space
            second_itr += 1
        print() # Prints a new line, nothing else
        iterator += 1

if __name__ == "__main__":
    inp = int(input("Please enter a number: "))
    right_triangle(inp)