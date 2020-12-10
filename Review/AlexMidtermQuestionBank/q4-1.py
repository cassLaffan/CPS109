#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Sum = 1/1 + 1/2 + 1/3 + ... + 1/n
# --------------------------------------------------------------
def series0(epsilon) :
    '''
    Return the value of n such that the above sum is 
    within epsilon of 4.23.
    For example, 
    if epsilon is 4, then return 1, since 1 the first term is within 4 of 4.23
    if epsilon is 3, then return 2, since 1 + 1/2 = 1.5 is within 3 of 4.23
    '''
    pass
    


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(series0(4), 1)
 def test2(self):
  self.assertEqual(series0(3), 2)
 def test3(self):
  self.assertEqual(series0(1), 14)
 def test4(self):
  self.assertEqual(series0(0.5), 23)
 def test5(self):
  self.assertEqual(series0(0.01), 38)


if __name__ == '__main__':
 unittest.main(exit=True)




# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
