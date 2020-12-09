import unittest

def q6(sentence) :
    '''
    Assumes sentence is a string.
    Returns a list of the most frequent words in the sentence,
    where words are obtained by sentence.split(),
    and each word is trimmed by removing trailing punctuation marks,
    where punctuation marks are any of the following letters: ';:.,!?'.

    Requirement: you must use a DICTIONARY to count frequency.

    For example, 
    q6('Hey diddle diddle the cat and the fiddle, the cow jumped over the moon')
    should return ['the'] since 'the' is the most frequent word.
    q6('red; blue!! blue red']
    should return ['red', 'blue'], where the items are in any order.
    '''
    pass

class myTests(unittest.TestCase):
    def test1(self):
        s = 'Hey diddle diddle the cat and the fiddle, the cow jumped over the moon'
        r = ['the']
        self.assertEqual(sorted(q6(s)), r)
    def test2(self):
        s = 'red, blue;, red! blue!!'
        r = ['blue', 'red']
        self.assertEqual(sorted(q6(s)), r)
    def test3(self):
        s = 'Red, blUe;, red! blue!!'
        r = ['Red', 'blUe', 'blue', 'red']
        self.assertEqual(sorted(q6(s)), r)

if __name__=='__main__':
    unittest.main(exit=True)
