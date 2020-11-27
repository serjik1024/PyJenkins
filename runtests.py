import unittest
import xmlrunner
import json
from book import Book


def runner(output='python_tests_xml'):
    return xmlrunner.XMLTestRunner(
        output=output
        )


books = Book()

def test_add():
    result = books.add_book('Book1', 'Author1')
    assert result

if __name__ == '__main__':
    print("Starting the test")
    runner().run(test_add())
    print("completed")
