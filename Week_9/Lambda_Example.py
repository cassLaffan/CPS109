'''
Here is an example of a lambda, which is an in-line, short, anonymous
function.
'''
if __name__ == "__main__":
    sum_of_squares = lambda x, y: x*x + y*y
    print(sum_of_squares(3, 8))
    print(sum_of_squares(2, 2))

    sum_of_squares = 10
    print(sum_of_squares)

    reversed_str = lambda a_str: a_str[::-1]
    print(reversed_str("hello"))
    print(reversed_str("Cassandra"))

    reversed_str = "eip"
    print(reversed_str)   

    another_math_example = lambda x, y, z: x * y * z
    another_var = another_math_example(1, 2, 3)
    print(another_var)