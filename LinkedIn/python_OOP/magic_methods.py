# Magic methods are special methods which have double underscores at the beginning and end of their names.
# They are also known as dunders.
# So far, the only one we have encountered is __init__, but there are several others.
# we can change the behavior of operators by defining magic methods.

# we will see __str__ and __repr__ in action.
# __str__ is used to return a user-friendly string representation of the object.


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author

    def __str__(
        self,
    ):  # __str__ is used to return a user-friendly string representation of the object. usually for the end user
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(
        self,
    ):  # __repr__ is used to return a developer-friendly string representation of the object. usually for the developers
        # commonly used for debugging
        return f"title={self.title}, author={self.author}, price={self.price}"


book1 = Book("War and Peace", "Leo Tolstoy", 40)
print(book1)  # OR print(str(book1)) # War and Peace by Leo Tolstoy, costs 40

print(repr(book1))  # title=War and Peace, author=Leo Tolstoy, price=40
