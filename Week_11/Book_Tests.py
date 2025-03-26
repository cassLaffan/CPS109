import Book_Exercise
import Manga_Exercise
import unittest

# Pascal case
class BookTests(unittest.TestCase):
    def setUp(self):
        self.book_one = Book_Exercise.Book()
        self.book_two = Book_Exercise.Book("Xyz", "ABC",
                                           "Any", "None", 100)
        self.manga_one = Manga_Exercise.Manga("Uzumaki", "Junji Ito", "Horror", "Dark Horse",
                    300, False, "Japan")
        self.manga_two = Manga_Exercise.Manga()
    
    def test1(self):
        self.book_two.double_page_length()
        self.assertEqual(self.book_two.page_length, 200)

    def test2(self):
        self.assertTrue(self.manga_one.has_anime(2000000))

    def test3(self):
        self.assertIsNone(self.book_one.author)

if __name__ == "__main__":
    unittest.main(exit=True)
    
    