import unittest
def recursive_palindrome(s) :
    '''
    Assumes that s is a string. Checks to see if s is a palindrome.
    If it is, returns True. Else, returns False.
    '''
    if len(s) == 1 or len(s) == 0:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        truth = s[0] == s[-1]
        return truth and recursive_palindrome(s[1:-1])

class PalinTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(recursive_palindrome('racecar'))
    def test2(self):
        self.assertFalse(recursive_palindrome('blue'))
    def test3(self):
        self.assertTrue(recursive_palindrome('madam'))

    '''
    Edge cases.
    '''
    def test4(self):
        self.assertTrue(recursive_palindrome(''))
    def test5(self):
        self.assertTrue(recursive_palindrome('eeeeeee'))

if __name__=='__main__':
    unittest.main(exit=True)
