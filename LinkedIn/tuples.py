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
