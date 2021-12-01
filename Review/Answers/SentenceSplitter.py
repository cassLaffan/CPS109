import unittest
import string

def split_sentence(sentence) :
    '''
    Assumes that sentence is a valid string. Returns a
    list of the most frequent words in the sentence, where
    words are obtained by sentence.split(). Each word is trimmed
    by removing trailing punctuation marks.
    '''
    word_dict = {}
    sentence_list = sentence.split()

    # Very short hand syntax, your results may vary
    # I personally hate list comprehension but you guys used it a lot
    sentence_list = [''.join(c for c in s if c not in string.punctuation) for s in sentence_list]

    for word in sentence_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    frequency_list = []

    # try/except here because you cannot take a max of an empty list
    try:
        maximum = max(word_dict.values())
    except:
        maximum = 0

    for search in sentence_list:
        if word_dict[search] == maximum and search not in frequency_list:
            frequency_list.append(search)

    return frequency_list

class myTests(unittest.TestCase):
    def test1(self):
        s = 'Hey diddle diddle the cat and the fiddle, the cow jumped over the moon'
        r = ['the']
        self.assertEqual(sorted(split_sentence(s)), r)
    def test2(self):
        s = 'red, blue;, red! blue!!'
        r = ['blue', 'red']
        self.assertEqual(sorted(split_sentence(s)), r)
    '''
    Edge cases are here.
    '''
    def test3(self):
        s = 'Red, blUe;, red! blue!!'
        r = ['Red', 'blUe', 'blue', 'red']
        self.assertEqual(sorted(split_sentence(s)), r)
    def test4(self):
        s = '!!'
        r = ['']
        self.assertEqual(split_sentence(s), r)
    def test5(self):
        self.assertEqual(split_sentence(''), [])

if __name__=='__main__':
    unittest.main(exit=True)