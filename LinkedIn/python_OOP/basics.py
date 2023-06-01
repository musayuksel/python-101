# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    @classmethod  # decorator to create a class method not an instance method
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    def __init__(self, title, author, pages, price=0.0, book_type="HARDCOVER"):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if book_type not in Book.BOOK_TYPES:
            raise ValueError(f"{book_type} is not a valid book type {Book.BOOK_TYPES}")
        else:
            self.book_type = book_type
        self.__secret = "This is a secret attribute"

    # getters and setters for the title attribute
    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def set_discount(self, amount):
        self._discount = amount  # _discount is a private variable

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


# TODO: create instances of the class
book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95, "HARDCOVER")
# book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95, "COMIC") # ValueError: COMIC is not a valid book type ('HARDCOVER', 'PAPERBACK', 'EBOOK')

# TODO: print the class and property
print(book1)
print(book1.getTitle())
book1.set_discount(0.25)
print(book1.get_price())

# print(book1.__secret)  # AttributeError: 'Book' object has no attribute '__secret'
print(book1._Book__secret)  # This is a secret attribute
