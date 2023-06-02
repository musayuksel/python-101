# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance


# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.price = price
#         self.author = author
#         self.pages = pages


# class Magazine:
#     def __init__(self, title, publisher, price, period):
#         self.title = title
#         self.price = price
#         self.period = period
#         self.publisher = publisher


# class Newspaper:
#     def __init__(self, title, publisher, price, period):
#         self.title = title
#         self.price = price
#         self.period = period
#         self.publisher = publisher


class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)  # call the base class constructor
        self.author = author
        self.pages = pages


# Newspaper and Magazine are have another common base class called Periodical
class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
