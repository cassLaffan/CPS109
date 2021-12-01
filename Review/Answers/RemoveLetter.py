import unittest

def remove_letter(s, removable_letter) :
    '''
    Assumes s is a string, and removable_letter is a letter.
    Returns a string obtained by removing any intances of
    removable_letter in the string. If the string doesn't
    have any instances of removable_letter, it simply returns
    the original string. Returns a ValueError if the values
    aren't typed correctly.
    '''
    try:
        if len(removable_letter) > 1:
            raise ValueError
        return s.replace(removable_letter, '')
    except Exception as error:
        raise ValueError

class RemoveTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(remove_letter('blue', 'x'), 'blue')
    def test2(self):
        with self.assertRaises(ValueError):
            remove_letter(529, 'a')
    def test3(self):
        with self.assertRaises(ValueError):
            remove_letter('red', 'xy')
    def test4(self):
        self.assertEqual(remove_letter('y', 'x'), 'y')
    def test5(self):
        self.assertEqual(remove_letter('', 'x'), '')
    def test6(self):
        self.assertEqual(remove_letter('z', 'z'), '')

if __name__=='__main__':
    unittest.main(exit=True)
    
