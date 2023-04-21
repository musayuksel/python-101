numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


def myFunc(fruit):
    print(fruit)
    return len(fruit)


fruitNameLengths = map(myFunc, ['apple', 'banana', 'cherry', "pear"])
print(list(fruitNameLengths))

#  We can use the filter method to filter a list
#  The filter method takes a function and a list as arguments
#  The function must return a boolean value
#  The filter method will return a list of all the items that return True


def isNameLong(fruitName):
    return len(fruitName) > 5


longFruitNames = filter(isNameLong, ['apple', 'banana', 'cherry', "pear"])
print(list(longFruitNames))
