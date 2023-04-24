numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


def myFunc(fruit: str):
    return len(fruit)


fruits = ['apple', 'banana', 'cherry', "pear"]
fruitNameLengths = map(myFunc, fruits)
print(list(fruitNameLengths))
# or we can pass callback function as lambda
# next function is the same as the previous one
fruitNameLengths = map(lambda fruit: len(
    fruit), fruits)
print(list(fruitNameLengths))
# also we can pass the index of the list
fruitNameWithIndex = map(
    lambda fruit, index: f'''{index} : {fruit}''', fruits, range(len(fruits)))
# The range will pass the index of the list
print(list(fruitNameWithIndex))

# fruitNameWithIndex = map(
#     lambda fruit, index: f'''{index} : {fruit}''', fruits, enumerate(fruits))
# # The enumerate will pass the index of the list
print(list(fruitNameWithIndex))


#  We can use the filter method to filter a list
#  The filter method takes a function and a list as arguments
#  The function must return a boolean value
#  The filter method will return a list of all the items that return True


def isNameLong(fruitName: str):
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
