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


# RANGE
#  The range function returns a list of numbers
#  The range function takes 3 arguments
#  The first argument is the start of the range (inclusive) (default 0)
#  The second argument is the end of the range (exclusive) (required) and the third argument is the step (default 1)
numbers2 = range(1, 10, 2)
print(list(numbers2))
doubleNumbers = map(lambda num: num * 2, numbers2)
print(list(doubleNumbers))
