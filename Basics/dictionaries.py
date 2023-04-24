#  A dictionary is a collection of key value pairs like objects in JavaScript
#  The key must be unique
#  The key can be a string, number or tuple
#  The value can be any data type

person = {
    "name": "Harry",
    "age": 17,
    "hobbies": ["football", "coding"],
    "address": {
        "street": "123 Main St",
        "city": "London"
    }
}

#  We can access the value of a key using square brackets
print(person["name"])  # Harry
print(person["address"]["city"])  # London
print(person.keys())  # dict_keys(['name', 'age', 'hobbies', 'address'])
# dict_values(['Harry', 17, ['football', 'coding'], {'street': '123 Main St', 'city': 'London'}])
print(person.values())

# UPDATE
#  We can add a new key value pair to a dictionary using square brackets
person["phone"] = "555-555-5555"
# {'name': 'Harry', 'age': 17, 'hobbies': ['football', 'coding'], 'address': {'street': '123 Main St', 'city': 'London'}, 'phone': '555-555-5555'}
print(person)
