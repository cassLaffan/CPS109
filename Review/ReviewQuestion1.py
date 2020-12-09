import unittest
import math

def q3(x, epsilon) :
    '''
    Returns guess, the approximate square root of x, such that 
    abs(guess**2 - x) < epsilon using Heron's algorithm, where 
    start with guess = x / 2 and improve guess to be (guess + x / guess) / 2
    '''
    guess = x / 2

    while(not(abs(guess**2 - x) < epsilon)):
        guess = (guess + x / guess) / 2

    return guess

class myTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(abs(q3(4, 0.1) - 2) <= 0.1)
    def test1(self):
        self.assertTrue(abs(q3(99, 0.1) - math.sqrt(99)) <= 0.1)
    def test2(self):
        self.assertTrue(abs(q3(999, 0.1) - math.sqrt(999)) <= 0.1)
    def test3(self):
        self.assertTrue(abs(q3(1, 0.1) - 1) <= 0.1)
    def test4(self):
        self.assertTrue(abs(q3(0.25, 0.01) - 0.5) <= 0.01)

if __name__=='__main__':
    unittest.main(exit=True)
