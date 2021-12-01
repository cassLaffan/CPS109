import unittest
'''
Returns the sum of the even numbers from n to 4*n, inclusive
even_addition(2) returns 20 since 2, 3, 4, 5, 6, 7, 8 -> 2 + 4 + 6 + 8 = 20
Do NOT assume that this function recieves a positive number, but do assume
that it recieves an integer.
'''

def even_addition(n) :
    pass

class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(even_addition(2), 20)
    def test2(self):
        self.assertEqual(even_addition(1), 6)
    def test3(self):
        self.assertEqual(even_addition(0), 0)
    def test4(self):
        self.assertEqual(even_addition(100), 37750)

if __name__=='__main__':
    print(even_addition(2), 'Expect 20')
    unittest.main(exit=True)
