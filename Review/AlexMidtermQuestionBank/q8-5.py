import unittest

def listMerge(listOfLists):
    '''
    Assume that listOfLists is a 2D list of lists.

    EX: [[12,22,44][12,9][2,4]]

    Create and return a new list that merges the lists with the following rules

    1. Create an empty output list

    2. Then, For each list in listOfLists:
        2.1. If list's sum is even, append the list's sum to the output list
        2.2. If list's sum is odd, append all of list's values to the output list
    
    For example, the above listOfLists would return

    [78,12,9,6]
    '''
    pass

class listMergeTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(listMerge([[12,22,44],[12,9],[2,4]]),[78,12,9,6])
    def test2(self):
        self.assertEqual(listMerge([[12],[44,11],[4,7,13]]),[12,44,11,24])
    def test3(self):
        self.assertEqual(listMerge([[88,19],[2,4,8,8,12],[8,7,14,12,12],[18,99]]),[88,19,34,8,7,14,12,12,18,99])
    def test4(self):
        self.assertEqual(listMerge([[],[2,4,8,9,12],[18,99]]),[2,4,8,9,12,18,99])
    def test5(self):
        self.assertEqual(listMerge([[],[],[]]),[])

if __name__ == '__main__':
    unittest.main(exit=True)