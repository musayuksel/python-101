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


book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)


print(book1.title)  # War and Peace
print(book1.author)  # Leo Tolstoy
