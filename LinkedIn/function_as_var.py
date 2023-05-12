# create 4 functions and call them in the main function
def func1():
    print("func1")
def func2():
    print("func2")
def func3():
    print("func3")
def func4():
    print("func4")

business_logic = [func1, func2, func3, func4]
# we don't need to worry about the business logic
# we just need to call the main function
def main():
    for func in business_logic:
        func()

# 
def do_something(func):
    print(func(5)+3)

do_something(lambda x: x+2)#similar to call back function in javascript