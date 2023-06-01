# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price=0.0):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # getters and setters for the title attribute
    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle


# TODO: create instances of the class
book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# TODO: print the class and property
print(book1)
print(book1.getTitle())
