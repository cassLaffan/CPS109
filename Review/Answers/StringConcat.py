import unittest

def string_concat(s) :
    '''
    Assumes s is a string. Returns a new string formed
    by concatenating i copies of the letter at position i,
    for each index position in string s. For example, 
    string_concat('dog') returns 'ogg' since 0 of 'd' and 1
    of 'o' and 2 of 'g'
    '''
    new_string = ""

    for i in range(len(s)):
        # new_string = new_string + s[i] * i
        new_string += s[i] * i

    return new_string

class StringTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(string_concat('dog'), 'ogg')
    def test2(self):
        self.assertEqual(string_concat('horse'), 'orrssseeee')
    def test3(self):
        self.assertEqual(string_concat('b'), '')
    def test4(self):
        self.assertEqual(string_concat('hippotamus'), 'ipppppooootttttaaaaaammmmmmmuuuuuuuusssssssss')
    '''
    Edge case here.
    '''
    def test5(self):
        self.assertEqual(string_concat(''), '')

if __name__=='__main__':
    unittest.main(exit=True)
