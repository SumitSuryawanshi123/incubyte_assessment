import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    
    def test_add_book(self):
        library = Library()
        book = Book("123456789", "Test Book", "Author Name", 2024)
        library.add_book(book)
        self.assertIn(book, library.get_available_books())
    
    def test_borrow_book(self):
       library = Library()
       book = Book("123456789", "Test Book", "Author Name", 2024)
       library.add_book(book)
       library.borrow_book("123456789")
       self.assertFalse(book.is_available)

if __name__ == "__main__":
    unittest.main()
