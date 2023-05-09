# List comprehensions are a concise way to create lists

my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)  # ['h', 'e', 'l', 'l', 'o']

my_list = [char for char in 'hello']  # ['h', 'e', 'l', 'l', 'o']

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, ...]
my_list2 = [num for num in range(0, 100) if num % 2 == 0]


def is_even(num):
    return num % 2 == 0


my_list2 = [num for num in range(0, 100) if is_even(num)]  # same as above
