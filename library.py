# library.py
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_available_books(self):
        return [book for book in self.books if book.is_available]
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                return
        raise Exception("Book not available")
    
    def return_book(self, isbn):
      for book in self.books:
          if book.isbn == isbn and not book.is_available:
              book.is_available = True
              return
      raise Exception("Book not found or not borrowed")
