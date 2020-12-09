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
    if len(s) == 1 or len(s) == 0:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        truth = s[0] == s[-1]
        return truth and q7(s[1:-1])

class myTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(q7('racecar'))
    def test2(self):
        self.assertFalse(q7('blue'))
    def test3(self):
        self.assertTrue(q7('madam'))

if __name__=='__main__':
    unittest.main(exit=True)
