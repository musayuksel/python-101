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


# function as a return value from another function
def logger(msg):
    return lambda: print('Log:', msg)

log_hi = logger('Hi!')
log_hi()

# function as a variable

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')
