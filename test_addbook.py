import json
from book import Book

books = Book()

def test_add():
    result = books.add_book('Book1', 'Author1')
    assert result
