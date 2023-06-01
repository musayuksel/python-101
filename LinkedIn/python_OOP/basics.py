# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price=0.0):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
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
book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# TODO: print the class and property
print(book1)
print(book1.getTitle())
book1.set_discount(0.25)
print(book1.get_price())

# print(book1.__secret)  # AttributeError: 'Book' object has no attribute '__secret'
