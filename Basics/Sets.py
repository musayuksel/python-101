# Duplicate values are not allowed
numbers = [1, 1, 1, 2, 15]
print(numbers)
print(set(numbers))

# Set intersection
#  We can use the & operator to get the items that are in both sets
lettersA = set(["a", "b", "c", "d"])
lettersB = set(["c", "d", "e", "d", "d"])
print(lettersA & lettersB)  # {'c', 'd'}

# Union
#  We can use the | operator to get the items that are in either set
# {'a', 'b', 'c', 'd', 'e', 'f'}
print(lettersA | lettersB)

# Difference
#  We can use the - operator to get the items that are in the first set but not the second
# {'a', 'b'}
print(lettersA - lettersB)

# Symmetric difference
#  We can use the ^ operator to get the items that are in either set but not both
# {'a', 'b', 'e', 'f'}
print(lettersA ^ lettersB)

# The ORDER of the items in the set is not guaranteed
