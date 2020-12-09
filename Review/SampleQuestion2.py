import unittest

def outside_of(a, b, epsilon) :
    '''
    Returns True if a and b are a distance greater than epsilon
    away from one another. For example:
    outside_of(5, 6, 2) -> False
    outside_of(5, 7, 1.5) -> True
    '''
    pass

class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(outside_of(5, 6, 2), False)
    def test1(self):
        self.assertEqual(outside_of(5, 7, 1.5), True)
    def test2(self):
        self.assertEqual(outside_of(1, 2, 1), False)
    def test3(self):
        self.assertEqual(outside_of(9, 9, 0), False)
    def test4(self):
        self.assertEqual(outside_of(9, 9, 100), False)
    def test5(self):
        self.assertEqual(outside_of(-90, 100, 0), True)

if __name__=='__main__':
    unittest.main(exit=True)
