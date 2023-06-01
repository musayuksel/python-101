number_list = range(-5, 5)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# MAP
doubled_list = map(
    lambda number: number * 2, number_list
)  # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]

print(list(doubled_list))

# FILTER
positive_list = filter(lambda number: number > 0, number_list)  # [1, 2, 3, 4]
