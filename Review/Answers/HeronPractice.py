import unittest
import math

def heron(x, epsilon) :
    '''
    Returns guess, the approximate square root of x, such that 
    abs(guess**2 - x) < epsilon using Heron's algorithm, where 
    start with guess = x / 2 and improve guess to be (guess + x / guess) / 2
    '''
    guess = x / 2

    while(not(abs(guess**2 - x) < epsilon)):
        guess = (guess + x / guess) / 2

    return guess

class HeronTests(unittest.TestCase):
    '''
    Remember, your test cases may vary. It is important to remember
    that there are many functions at your disposal in this library.
    '''
    def test0(self):
        self.assertTrue(abs(heron(4, 0.1) - 2) <= 0.1)
    def test1(self):
        self.assertTrue(abs(heron(99, 0.1) - math.sqrt(99)) <= 0.1)
    def test2(self):
        self.assertTrue(abs(heron(999, 0.1) - math.sqrt(999)) <= 0.1)
    def test3(self):
        self.assertTrue(abs(heron(1, 0.1) - 1) <= 0.1)
    def test4(self):
        self.assertTrue(abs(heron(0.25, 0.01) - 0.5) <= 0.01)

if __name__=='__main__':
    unittest.main(exit=True)
