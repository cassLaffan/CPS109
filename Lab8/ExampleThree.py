import unittest
# Notice how the FIRST THING I do in my program is import the necessary
# library and I (should) only import it once.

'''This example of bad programming practice involves us writing our
tests AFTER designing our program. This is bad practice and is to be
avoided. Always write your code to be black box tested.'''

def our_function(a, b):
    '''fnction mustlplies a and b then return c'''
    c = a * b
    return c

class MyTests(unittest.TestCase):
    pass

# There is a problem with the first line in the main. You should only
# import once, and your imports should be at the top of the code.
if __name__ == "__main__":
    import unittest
    unittest.main(exit=True)
