import unittest
import ExampleTwo

class my_tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(ExampleTwo.count_brackets("{{}}"), True)
    def test2(self):
        self.assertEqual(ExampleTwo.count_brackets("}}{{"), False)
    def test3(self):
        self.assertEqual(ExampleTwo.count_brackets("}}}}"), False)
    def test4(self):
        self.assertEqual(ExampleTwo.count_brackets("{}{}{}{}"), True)
    def test5(self):
        self.assertEqual(ExampleTwo.count_brackets("{{}}{}{{}}"), True)


if __name__ == '__main__':
    unittest.main(exit=True)