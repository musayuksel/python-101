# Multiple line strings
# Strings can be written in multiple lines using triple quotes
# The triple quotes can be single or double quotes
# The new lines will be included in the string
comment = """This is a
multi-line comment"""
print(comment)

#  We can use the format method to format a string


def dynamicString(name, age):
    # return "My name is {} and I am {} years old".format(name, age)
    return f'''My name is {name} and I am {age} years old'''


print(dynamicString("Harry", 17))
