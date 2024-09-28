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
       
    def test_return_book(self):
        library = Library()
        book = Book("123456789", "Test Book", "Author Name", 2024)
        library.add_book(book)
        library.borrow_book("123456789")
        library.return_book("123456789")
        self.assertTrue(book.is_available)
    
    def test_view_available_books(self):
        library = Library()
        book1 = Book("123456789", "Test Book 1", "Author 1", 2024)
        book2 = Book("987654321", "Test Book 2", "Author 2", 2023)
        library.add_book(book1)
        library.add_book(book2)
        library.borrow_book("123456789")
        available_books = library.get_available_books()
        self.assertIn(book2, available_books)
        self.assertNotIn(book1, available_books)

if __name__ == "__main__":
    unittest.main()
