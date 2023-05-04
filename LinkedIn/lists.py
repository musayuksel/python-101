# Arrays in Python are called list
print(type([]))  # <class 'list'>
print(type((2, 3)))  # <class 'tuple'> tuple is immutable


# 1. Create a list of 5 fruits objects
# Sort the list in alphabetical order
# Reverse the list
# Sort the list with weight

class Fruit:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __repr__(self):  # official string representation of an object
        return f'Fruit({self.name}, {self.weight})'

    def __str__(self):  # human-readable, or informal, string representation of an object
        return f'Fruit name is :{self.name}, and the weight is: {self.weight}'


fruits = [
    Fruit('apple', 10),
    Fruit('banana', 5),
    Fruit('cherry', 20),
    Fruit('pear', 15),
    Fruit('orange', 25)
]

# fruits.sort(key=lambda fruit: fruit.name) #inplace
# not inplace and return a new list
sorted_with_name = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# reverse=True is optional and it is False by default (ascending)
print(sorted_with_name)

sorted_with_weight = sorted(fruits, key=lambda fruit: fruit.weight)
print(sorted_with_weight)
print(str(fruits[0]))  # Fruit name is :apple, and the weight is: 10
print(repr(fruits[0]))  # Fruit(apple, 10)


# Range
# The range function returns a list of numbers
# The range function takes 3 arguments
# The first argument is the start of the range (inclusive) (default 0)
# The second argument is the end of the range (exclusive) (required) and the third argument is the step (default 1)
numbers2 = range(1, 10, 2)  # [1, 3, 5, 7, 9]
