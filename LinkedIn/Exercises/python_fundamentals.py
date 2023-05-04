# 1) Create a function that takes a dictionary of ANDi names and returns a list of their names in alphabetical order.
example_input = {'ANDi1': 'John', 'ANDi2': 'Bob', 'ANDi3': 'Alice'}
# example output: ['Alice', 'Bob', 'John']


def sort_dict_names(dictionary):
    return sorted(dictionary.values())


sorted_andi_names = sort_dict_names(example_input)
print(sorted_andi_names)  # ['Alice', 'Bob', 'John']

# If we want to sort a list of andi dictionaries by their names, we can use the sorted function with a key argument
example_input_andis = [{'name': 'John'}, {'name': 'Bob'}, {'name': 'Alice'}]


def sort_andis_by_name(andis):
    return sorted(andis, key=lambda andi: andi['name'])


sort_dict_names = sort_andis_by_name(example_input_andis)
# [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'John'}]
print(sort_dict_names)
