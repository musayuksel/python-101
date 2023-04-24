# print("hello world")
1  # int
2.5  # float
"hello"  # string
True  # boolean
None  # null


# While loop
while True:
    try:
        age = int(input("What is your age? "))
        break
    except ValueError:
        print("Please enter a number")

i = 0
while i < age:
    print(str(i) + " years old!")
    i += 1


# BREAK and CONTINUE
# We can use them with for and while loops
number = 0

while (number < 10):
    number += 1
    if number % 2 == 0:  # if number is even
        continue
        # break # break the loop
    print(number)
