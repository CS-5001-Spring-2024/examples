from library import Library
from book import Book

def main():
	library = Library()
	
	book = Book('Holly', 'Stephen King', 5)
	library.add_book(book)

	book = Book('Harry Potter', 'JK Rowling', 10)
	library.add_book(book)

	library.check_out('Harry Potter')
	
	# view the number of copies of HP available
	print(library.get_num_copies('Harry Potter')) # 9



if __name__ == '__main__':
	main()
