import unittest

def q5(sentence) :
    '''
    Assumes sentence is a string.
    Returns a list of all the words in sentence, where a word is a token
    separated by white space, (you can use sentence.split()), and then
    for each word, make it lowercase and remove any character that is not 
    alpha-numeric (a-z or 0-9).

    For example, 
    q5('"The Plague" (French: "La Peste"), 1947, by Albert Camus.')
    should return ['the', 'plague', 'french', 'la', 'peste', '1947', 'by', 'albert', 'camus']
    q5('Red@Dragon....ca is great!')
    should return ['reddragonca', 'is', 'great']
    '''
    word_list = sentence.split()
    new_list = []
    alpha_numeric = "0123456789abcdefghijklmnopqrstuvwxyz"

    for word in word_list:
        word = word.lower()
        new_string = ""
        for letter in word:
            if letter in alpha_numeric:
                new_string += letter
        new_list.append(new_string)

    return new_list


class myTests(unittest.TestCase):
    def test1(self):
        s = '"The Plague" (French: "La Peste"), 1947, by Albert Camus.'
        r = ['the', 'plague', 'french', 'la', 'peste', '1947', 'by', 'albert', 'camus']
        self.assertEqual(q5(s), r)
    def test2(self):
        s = 'Hey diddle diddle the cat and the fiddle, the cow jumped over the moon.'
        r = ['hey', 'diddle', 'diddle', 'the', 'cat', 'and', 'the', 'fiddle', 'the', 'cow', 'jumped', 'over', 'the', 'moon']
        self.assertEqual(q5(s), r)
    def test3(self):
        s = 'The end of the free lunch??!!'
        r = ['the', 'end', 'of', 'the', 'free', 'lunch']
        self.assertEqual(q5(s), r)
    def test4(self):
        s = 'email address: blue@gmail.com'
        r = ['email', 'address', 'bluegmailcom']
        self.assertEqual(q5(s), r)
    def test5(self):
        s = 'Red@Dragon....ca is great!'
        r = ['reddragonca', 'is', 'great']
        self.assertEqual(q5(s), r)

if __name__=='__main__':
    unittest.main(exit=True)
