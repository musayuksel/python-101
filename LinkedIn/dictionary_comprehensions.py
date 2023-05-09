# 
animal_list = ['dog', 'cat', 'parrot', 'hamster', 'rabbit', 'goldfish']

# Create a list of the first letter of each animal in animal_list
# using a dictionary comprehension
first_letters = { animal[0]:animal for animal in animal_list}
print(first_letters)
print(">>>>>>>>>>>>>>")
animal_list_formatted = [{"first_letter":key, "name":value} for key,value in first_letters.items()]
print("animal_list_formatted:   ",animal_list_formatted)