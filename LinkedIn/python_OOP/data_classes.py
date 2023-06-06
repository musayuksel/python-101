# after python3.7

# This is standard class
# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price

from dataclasses import dataclass


# This is a data class
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"


book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
book2 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)


print(book1.title)  # War and Peace
print(book1.author)  # Leo Tolstoy

# it will automatically generate __init__ and __repr__ methods
print(
    book1
)  # Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=39.95)

# it will automatically generate __eq__ method
print(book1 == book2)  # True
