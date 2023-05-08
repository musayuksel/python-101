# SETS
mySet = {1, 2, 3, 4, 5, 5, 5, 5, 5}  # {1, 2, 3, 4, 5}
# OR
mySet = set([1, 2, 3, 4, 5, 5, 5, 5, 5])  # {1, 2, 3, 4, 5}
print(mySet)
# IF WE WANT TO CONVERT TO A LIST AGAIN
myList = list(mySet)  # [1, 2, 3, 4, 5]
print(myList)
# print(mySet[0])  # TypeError: 'set' object is not subscriptable
# SO WE CAN USE discard() OR remove() TO REMOVE AN ITEM FROM THE SET


# TUPLES
myTuple = ('a', 'b', 'c', 'd', 'e')
print(myTuple[0])  # a # we can access the tuple by index
print(myTuple[1:3])  # ('b', 'c') # we can access a range of items
# myTuple[0]='z' # TypeError: 'tuple' object does not support item assignment

# Wy we use tuples?
# 1. Tuples are faster than lists
# 2. Tuples are immutable
# 3. Tuples are used to return multiple values from a function


def get_person():
    name = "Harry"
    age = 30
    country = "UK"
    return name, age, country  # return a tuple


harry = get_person()
print(harry)  # ('Harry', 30, 'UK')
print(type(harry))  # <class 'tuple'>
# 4. Tuples are used to format strings
