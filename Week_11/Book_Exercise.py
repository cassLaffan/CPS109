class Book:
	# Total books in the library
	total_books = 0

	def __init__(self, t, a, g, p, pl):
		self.title = t
		self.author = a
		self.genre = g
		self.publisher = p
		self.page_length = pl
		Book.total_books = Book.total_books + 1

	def __str__(self):
		return f"Title: {self.title} \nAuthor: {self.author}"

	def change_author(self, new_author):
		self.author = new_author
	
	def double_page_length(self):
		self.page_length = self.page_length * 2
	
	def reset_count(self):
		Book.total_books = 0

	@property
	def maybe_double(self):
		return self.page_length * 2

if __name__ == "__main__":
	a_book = Book("War and Peace", "Tolstoy",
			   "Drama", "Tsar", 1000)
	second_book = Book("Metamorphosis", "Kafka",
					"Drama", "Penguin House", 100)
	print(a_book)

	print(a_book.page_length)
	a_book.change_author("Cassandra Laffan")
	print(a_book)
	print(a_book.maybe_double)
	print(Book.total_books)
	a_book.reset_count()
	print(Book.total_books)
