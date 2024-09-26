'''
In this file, we're going to explore one of python's other
iterable types: sets! Sets contain only unique data entries.
'''

if __name__ == "__main__":
    # Using curly braces
    fruits = {'blueberry', 'banana', 'cherry', 'strawberry'}

    # Using the set constructor
    more_fruits = set(['orange', 'kiwi', 'banana']) 

    # Add a mango to the set
    fruits.add('mango')

    # Remove banana
    # fruits.remove('banana')

    # Remove will raise an error, however, discard won't!
    fruits.discard('banana')

    combined_froot = fruits | more_fruits 
    print(combined_froot)

    # Get the intersection of sets
    common_fruit = fruits & more_fruits

    # Get the difference between two sets
    diff = fruits - more_fruits
