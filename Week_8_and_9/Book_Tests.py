import Book_Exercise
import Manga_Exercise
import unittest

class Book_Tests(unittest.TestCase):
    def setUp(self):
        self.book_one = Book_Exercise.Book()
        self.book_two = Book_Exercise.Book("Roadside Picnic", "Brother", "1970", 200)
    
    def test1(self):
        self.assertFalse(self.book_one == self.book_two)

    def test2(self):
        self.book_two.mark_page(100)
        self.assertEqual(self.book_two.current_page, 100)
    
    def test3(self):
        self.assertEqual(self.book_one.author, None)

if __name__ == "__main__":
    unittest.main(exit=True)