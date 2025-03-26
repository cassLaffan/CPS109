import Book_Exercise
import Manga_Exercise
import unittest

class Book_Tests(unittest.TestCase):
    def setUp(self):
        self.book_one = Book_Exercise.Book()
        self.book_two = Book_Exercise.Book()
    
    