'''
Recursively sorts a tuple containing letters and
returns a sorted version of the tuple. Does not
require a list.

Reading on quicksort:

https://www.geeksforgeeks.org/quick-sort/

https://en.wikipedia.org/wiki/Quicksort
'''
def tuple_sort(letter_tuple):
    # Our base case!
    if len(letter_tuple) <= 1:
        return letter_tuple
    # Our recursive step
    else:
        # A few interesting things are happening here. First, I have a \ that breaks up
        # the line. This makes your code much easier to read and allows you to conintue a line
        # later.

        # Second, I am concatonating two tuples. Remember, + allows two tuples to be merged,
        # producing a new one.

        # We also have list comprehension! I'll be going over that in week 9.
        # For now, feel free to read about it here: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        return tuple_sort([e for e in letter_tuple[1:] if e <= letter_tuple[0]]) +\
             [letter_tuple[0]] + tuple_sort([e for e in letter_tuple[1:] if e > letter_tuple[0]])


if __name__ == "__main__":
    print(tuple_sort(('c', 'a')))
    print(tuple_sort(('c', 'r', 'a')))
    print(tuple_sort(('c', 'r', 'a', 's')))
    print(tuple_sort(('c', 'r', 'a', 's', 'a')))
    print(tuple_sort(('c', 'r', 'a', 's', 'a', 'b')))
