import unittest
# Notice how the FIRST THING I do in my program is import the necessary
# library and I only import it once.

'''This is how you correctly design a program. You write the tests FIRST.'''

def our_function(a, b):
    '''A function that multiples a and b.'''
    pass

class MyTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(our_function(0, 0), 0)
    def test2(self):
        self.assertEqual(our_function(2, 3), 6)
    def test3(self):
        self.assertEqual(our_function(3, 3), 9)
    def test4(self):
        self.assertEqual(our_function(-1, 9), -9)
    def test5(self):
        self.assertEqual(our_function(-1, -1), 1)

if __name__ == "__main__":
    unittest.main(exit=True)