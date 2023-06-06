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
# dataclass(frozen=True) # if we want to make it immutable
class Book:
    title: str
    author: str
    pages: int
    price: float = 39.95  # default value

    def bookinfo(self):
        return f"{self.title}, by {self.author}"

    # POST INIT
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
book2 = Book("War and Peace", "Leo Tolstoy", 1225)


print(book1.title)  # War and Peace
print(book1.author)  # Leo Tolstoy

# it will automatically generate __init__ and __repr__ methods
print(
    book1
)  # Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=39.95)

print(book1.description)  # War and Peace by Leo Tolstoy, 1225 pages
# it will automatically generate __eq__ method
print(book1 == book2)  # True
