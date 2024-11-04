import unittest
import Balanced_Brackets

class my_tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Balanced_Brackets.count_brackets("{{}}"), True)
    def test2(self):
        self.assertEqual(Balanced_Brackets.count_brackets("}}{{"), False)
    def test3(self):
        self.assertEqual(Balanced_Brackets.count_brackets("}}}}"), False)
    def test4(self):
        self.assertEqual(Balanced_Brackets.count_brackets("{}{}{}{}"), True)
    def test5(self):
        self.assertEqual(Balanced_Brackets.count_brackets("{{}}{}{{}}"), True)


if __name__ == '__main__':
    unittest.main(exit=True)