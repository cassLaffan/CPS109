'''
Here, we will be using a for loop to iterate
over some basic iterable types in Python.
'''

if __name__ == "__main__":
    # List example
    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        print(f"I like {fruit}") # Hey, another fstring!

    # String example
    for char in "hello":
        print(char)

    # Tuple example
    coords = (1, 2, 3)
    for coord in coords:
        print(coord)

