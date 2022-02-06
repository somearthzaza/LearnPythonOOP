
class Catalog:
    def __init__(self):
        self._books = []
        
    @property
    def books(self):
        return self._books

    def search(self, search_key):
        get_list = []
        for book in self._books:
            if search_key == book.isbn or search_key == book.dds_number or search_key == book.title:
                get_list.append(book)
            for author in book.authors:
                if search_key == author.name:
                    get_list.append(book)
        return get_list

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only instance of class Book")
        return self

    def delete_book(self, search_key):
        for index, book in enumerate(self._books):
            if search_key == book.isbn:
                print(f"delete {book.isbn} {book.subject}")
                self._books.pop(index)
                break


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
            print("string only")


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
    
    @subject.setter
    def subject(self, subject):
        if isinstance(subject, str):
            self._subject = subject
        else:
            print("string only")

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            print("string only")

    @property
    def isbn(self):
        return self._ISBN

    @property
    def dds_number(self):
        return self._dds_number


author1 = Author("chin")
author2 = Author("earth")
horror = Catalog()
book1 = Book(1, [author1, author2], "adventure", "horor", 1001)
book2 = Book(2, [author1, author2], "star wars", "sci-fi", 1002)
horror.add_book(book1).add_book(book2)
print(horror.books)
print(horror.search("chin"))
