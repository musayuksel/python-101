number_list = range(-5, 5)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# MAP
doubled_list = map(
    lambda number: number * 2, number_list
)  # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]

print(list(doubled_list))

# FILTER
positive_list = filter(lambda number: number > 0, number_list)  # [1, 2, 3, 4]


# List Comprehension
doubled_list = [
    number * 2 for number in number_list
]  # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]

# List Comprehension with condition
positive_list = [number for number in number_list if number > 0]  # [1, 2, 3, 4]

# REDUCE
from functools import reduce


# reduce(acc, iterable, startValueForAccumulator)
def accumulator(acc, number):
    print(acc, "---", number)
    return acc + number


sum = reduce(accumulator, number_list, 0)  # 0
# 0 --- -5
# -5 --- -4
# -9 --- -3
# -12 --- -2
# -14 --- -1
sum2 = reduce(accumulator, number_list)  # 0
# -5 --- -4
# -9 --- -3
# -12 --- -2
# -14 --- -1

sum3 = reduce(lambda acc, number: acc + number, number_list, 0)  # 0
