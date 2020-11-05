import unittest
import ExampleOne

'''
What the heck is going on here?
This, in short: a built in class definition that lets
you automatically test your code. You writ things this way,
Python does the leg work for you.
'''
class my_tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(ExampleOne.mostfrequent([5, 2, 9, 2, 9, 1, 18, 9, 3]), 9)
    def test2(self):
        self.assertEqual(ExampleOne.mostfrequent(['cat', 'dog', 'dog', 'cat', 'cat']), 'cat')
    def test3(self):
        self.assertEqual(ExampleOne.mostfrequent([5]), 5)
    def test4(self):
        self.assertEqual(ExampleOne.mostfrequent([1, 2, 3, 3, 2, 1]), 1)
    def test5(self):
        self.assertEqual(ExampleOne.mostfrequent([(5, 5, 5), (3, 2, 1), (5, 5, 5)]), (5, 5, 5))


if __name__ == '__main__':
    unittest.main(exit=True)