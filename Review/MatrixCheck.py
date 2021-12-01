import unittest
'''
Assume that matrix is a 2D array of integers.
Write a function that returns True if the second
last number of the second row occurs in any other rows.

For example, 
matrix_check([[5, 6, 7, 2], [9, 8, 4, 22]]) -> False
matrix_check([[7, 6, 9, 2], [9, 4, 7, 22], [7, 1, 6, 99]]) -> True

Hint: use negative indicies for this one.
'''

def matrix_check(matrix) :
    pass

class MatrixTests(unittest.TestCase):
    def test1(self):
        m = [[5, 6, 7, 2], [9, 8, 4, 22]]
        self.assertFalse(matrix_check(m))
    def test2(self):
        m = [[7, 6, 9, 2], [9, 4, 7, 22], [7, 1, 6, 99]]
        self.assertTrue(matrix_check(m))

if __name__=='__main__':
    unittest.main(exit=True)