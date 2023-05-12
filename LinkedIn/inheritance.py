# list is a python built-in data structure, basically a class

class MyList(list): # class MyList inherits from class list
    def __init__(self):
        super().__init__() # make sure to call the parent class constructor
        self.counter = 0 # add a new attribute to the class
    def remove_min(self):
        self.remove(min(self))

my_list = MyList()
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)

print(my_list)
my_list.remove_min()
print(my_list)
print(my_list.counter)