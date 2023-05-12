def sum_all(*args, **kwargs):
    print(locals())
    print(args) # tuple
    print(kwargs) # dict
    print( "SUM :", sum(args))
    # if there is a key called "name" in kwargs, print it
    if "name" in kwargs:
        print("NAME: ", kwargs["name"])

sum_all(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, name="John", age=30, city="New York")
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# {'name': 'John', 'age': 30, 'city': 'New York'}

def sum_all_with_local( *args, **kwargs):
    print(locals())
    # print(sum(locals()["args"]))

sum_all_with_local(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, name="John", age=30, city="New York")