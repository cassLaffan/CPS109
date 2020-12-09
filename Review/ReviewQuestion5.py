import unittest

def q7(s) :
    '''
    Assumes s is a string that has no punctuation and no blanks
    and is all lowercase.
    Returns True if s is a palindrome, False otherwise.

    You must use RECURSION to solve the problem.

    For example, 
    q7('racecar') is True
    q7('blue') is False
    '''
    pass

class myTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(q7('racecar'))
    def test2(self):
        self.assertFalse(q7('blue'))
    def test3(self):
        self.assertTrue(q7('madam'))

if __name__=='__main__':
    unittest.main(exit=True)
