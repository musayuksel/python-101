class Dog:
# STATIC CLASS ATTRIBUTEs and private class attributes
    species = "Canis familiaris" # class attribute
    _legs = 4 # private class attribute
    def __init__(self, name, age):
        # special method that is called when you create a new object
        self.name = name
        self.age = age

    # getter for private class attribute
    @property
    def get_legs(self):
        return self._legs
    
    @staticmethod # decorator !!!! static method
    # static method is a method that doesn't take self as an argument
    def speak(sound):
        # static method
        print(f"{sound}")

    def bark(self):
        print(f"{self.name} says woof!")


my_dog = Dog("Rex", 5)
my_dog.bark()  # We call it without passing any arguments because the self argument is passed automatically

# print(my_dog._legs) #we don't use with this way
print(my_dog.get_legs) # we use with this way

# calling static method
Dog.speak("woof woof")
my_dog.speak("woof woof") # we can call static method with object