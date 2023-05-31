# we can pass function as an argument to another function
# we can return a function from another function
# we can assign a function to a variable
# we can store a function in a data structure such as list, tuple, dictionary, set

# function as an argument to another function
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


# function as a variable

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')


#RETURNING FUNCTIONS FROM FUNCTIONS
def logger(msg):
    def log_message(name):
        print(f'{name}: {msg}')
    return log_message

logger('Hi!')("Musa")# AKA currying
# print(log_hi)

# CLOSURES
# A closure is a record storing a function together with an environment

def create_counter():
    count = 0

    def get_count():
        return count

    def increment():
        nonlocal count # nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
        count += 1
        return count
    return (get_count,increment)

get_count, increment = create_counter()
print(increment())
print(get_count())
