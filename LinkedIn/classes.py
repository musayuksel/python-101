class Dog:
    def __init__(self, name, age):
        # special method that is called when you create a new object
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")


my_dog = Dog("Rex", 5)
my_dog.bark()  # We call it without passing any arguments because the self argument is passed automatically
