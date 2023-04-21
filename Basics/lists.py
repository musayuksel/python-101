names = ["Harry", "Ron", "Hermione"]
#  We can use negative numbers to access the list from the end
print(names[-1])
#  We can also use a range to access a part of the list
print(names[0:2])

# Methods
#  We can use the append method to add an item to the end of the list
names.append("Draco")
print(names)
# we can add insert to add an item to a specific index
names.insert(1, "Neville")
print(names)

#  We can use the remove method to remove an item from the list
names.remove("Draco")
print(names)

#  We can use the pop method to remove an item from the end of the list
names.pop()
print(names)

# We can use the in method to check if an item is in the list
print("Harry" in names)  # True

# We can use the len method to get the length of the list
print(len(names))  # 3
