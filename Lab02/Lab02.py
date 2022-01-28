class Catalog:
    def __init__(self):
        self._books = []

    def search(self, search_key):
        for book in self._books:
            if search_key == book.isbn or search_key == book.dds_number or search_key == book.title:
                print(
                    f"found {book.isbn} {book.title} {book.dds_number} {book.subject}")
            for author in book.authors:
                if search_key == author.name:
                    print(
                        f"found {book.isbn} {book.title} {book.dds_number} {book.subject}")

    def add_book(self, isbn, authors, title, subject, dds_number):
        self._books.append(Book(isbn, authors, title, subject, dds_number))
        return self

    def delete_book(self, search_key):
        for index, book in enumerate(self._books):
            if search_key == book.isbn:
                self._books.pop(index)


class Author:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("String only")


class Book:

    def __init__(self, isbn, authors, title, subject, dds_number):
        self._ISBN = isbn
        self._authors = authors
        self._title = title
        self._subject = subject
        self._dds_number = dds_number

    @property
    def authors(self):
        return self._authors

    @property
    def subject(self):
        return self._subject

    @property
    def title(self):
        return self._title

    @property
    def isbn(self):
        return self._ISBN

    @property
    def dds_number(self):
        return self._dds_number


author1 = Author("chin")
author2 = Author("earth")
horor = Catalog()
horor.add_book(1, [author1, author2], "adventure", "horor", 1001).add_book(
    2, [author2], "star wars", "sci-fi", 1002)
horor.search(1001)
