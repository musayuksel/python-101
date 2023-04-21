# print("hello world")

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
