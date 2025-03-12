class Book:
    def __init__(self, bt=None, au=None, pd=None, pl=None):
        '''This is our Book constructor!'''
        self.book_title = bt
        self.author = au
        self.pub_date = pd
        self.page_length = pl
        self.current_page = 0

    def __str__(self):
        return f"Title: {self.book_title} \nAuthor: {self.author}\n"

    def mark_page(self, pages_read):
        self.current_page += pages_read

    @property
    def peak_next_page(self):
        return self.current_page + 1

if __name__ == "__main__":
    our_first_book = Book("War and Peace", "Tolstoy", "Jan 1 1867", 600)

    print(our_first_book, end="")
    print(f"Our current page is: {our_first_book.current_page}")

    our_first_book.mark_page(200)

    print(f"Our current page is: {our_first_book.current_page}")

    print(f"The next page is: {our_first_book.peak_next_page}")

    print(f"Our current page is: {our_first_book.current_page}")

