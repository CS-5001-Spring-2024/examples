
from book import Book

class Library:

	def __init__(self):
		self.bookshelf = {}

	# def add_book(self, title, author, num_copies):
	# 	book = Book(title, author, num_copies)	
	# 	self.bookshelf[title] = book	

	def add_book(self, book):
		# TODO: make sure the book isn't already on the shelf
		self.bookshelf[book.title] = book

	def check_out(self, title):
		self.bookshelf[title].check_out()

	def get_num_copies(self, title):
		return self.bookshelf[title].num_copies		
