import unittest
from unittest.case import TestCase
'''
Here is the simplest implementation of a recursive factorial function.
There are five test cases, two of which are edge cases. Your answers
may vary slightly. The commonality should be that all of your tests
pass.
'''

def factorial(num):
    # Base case is num == 0
   if(num <= 1):
       return 1
   else:
       new_num = num * factorial(num - 1)
       return new_num


class FacTest(unittest.TestCase):
    '''
    The following two tests are considered edge cases.
    '''
    def test1(self):
        self.assertEqual(factorial(0), 1)
    def test2(self):
        self.assertEqual(factorial(-1), 1)
    '''
    The next three are just regular test cases.
    '''
    def test3(self):
        self.assertEqual(factorial(2), 2)
    def test4(self):
        #notice how I take advantage of a different function in this library
        self.assertNotEqual(factorial(10), 1)
    def test5(self):
        self.assertEqual(factorial(11), 39916800)

if __name__ == "__main__":
    unittest.main(exit=True)