'''
Here, we'll play around with Tuples!
'''

# Tuple Functions Demo

if __name__ == "__main__":
    # Create a tuple
    my_tuple = (1, 2, 3, 2, 4, 2)

    # How man times does 2 occur?
    count_of_twos = my_tuple.count(2)
    print("Count of 2 in the tuple:", count_of_twos)

    # Find the index of 3
    index_of_two = my_tuple.index(3)
    print("First index of 3 in the tuple:", index_of_two)

    # Tuple unpacking
    a, b = (1, 2)
    print("Unpacked values: a =", a, ", b =", b)

