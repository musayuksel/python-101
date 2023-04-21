my_number = input("Enter a number: ")
try:
    my_number = int(my_number)
    if my_number % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ValueError:
    print(f''' {my_number} is not a number.
    Please enter a number''')
