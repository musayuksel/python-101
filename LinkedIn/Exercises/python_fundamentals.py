######### EXERCISE 1 #########
# 1) Create a function that takes a dictionary of ANDi names and returns a list of their names in alphabetical order.
example_input = {'ANDi1': 'John', 'ANDi2': 'Bob', 'ANDi3': 'Alice'}
# example output: ['Alice', 'Bob', 'John']


def sort_dict_names(dictionary: dict) -> list:
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

######### EXERCISE 2 #########
# 2) I'm trying to watch some LinkedIn Learning videos to complete my Python Learning Pathway but I keep getting distracted by meme compilations, music recommendations, pets and more on Slack.
# Your job is to help me create a function that takes a string and checks to see if it contains the following words or phrases: "Dog", "pet", "music", "Funny meme", "Listen to this"
# If it does, return "NO!" Otherwise, return "Safe watching!"


example_input = "I'm trying to watch a video on Python but I keep getting distracted by a dog"
# NO!
example_input2 = "I'm trying to watch a video on Python"  # Safe watching!


def is_destructive(string: str) -> str:
    words = ["Dog", "pet", "music", "funny meme", "listen to this"]
    for word in words:
        if word.lower() in string.lower():
            return "NO!"
    return "Safe watching!"


print(is_destructive(example_input))  # NO!
print(is_destructive(example_input2))  # Safe watching!


######### EXERCISE 3 #########
# 3) Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.
# In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.
example_message = "anddigital is cool"  # "4ndd1g1t4l 15 c00l"


def hacker_speak(message: str) -> str:
    letters = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
    secret_message = map(
        lambda letter: letters[letter] if letter in letters else letter, list(message))
    return "".join(secret_message)


hacker_speak_message = hacker_speak(example_message)
print(hacker_speak_message)  # 4ndd1g1t4l 15 c00l
