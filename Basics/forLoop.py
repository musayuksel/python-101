numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


def myFunc(fruit):
    print(fruit)
    return len(fruit)


x = map(myFunc, ['apple', 'banana', 'cherry'])
print(list(x))
