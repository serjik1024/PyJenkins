import json


class Book:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = {}
        new_book["Title"] = title
        new_book["Author"] = author
        self.books.append(new_book)
        print("Book: {0}".format(new_book))
        return json.dumps(new_book)
        #return False

    def json_list(self):
        return json.dumps(self.books)
