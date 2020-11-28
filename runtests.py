import unittest
import xmlrunner
import json
from book import Book

books = Book()

def runner(output):
    return xmlrunner.XMLTestRunner(
        output=output
        )

class TestBook(unittest.TestCase):
	
	def test_add(self):
		result = books.add_book('Book1', 'Author1')
		print(result)
		assert result

if __name__ == '__main__':
    print("Starting the runner test")
    with open('results.xml', 'wb') as output:
        runner(output).run(unittest.main())
    #unittest.main()
    print("completed")
