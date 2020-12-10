def equalPairs(a,b,c,d):
    '''
    Assume a, b, c and, d are all integers.
    Return True if the integers can be split into two pairs
    that equal each other when added together.

    For example (12,2,6,8) would return true, as 
    12+2 = 14 and 6+8 = 14
    '''
    pass
    

class equalPairsTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(equalPairs(12,8,6,2), True)
    def test2(self):
        self.assertEqual(equalPairs(12,3,6,8), False)
    def test3(self):
        self.assertEqual(equalPairs(12,12,12,12), True)
    def test3(self):
        self.assertEqual(equalPairs(6,10,14,10), True)
    def test3(self):
        self.assertEqual(equalPairs(1,2,8,12), False)