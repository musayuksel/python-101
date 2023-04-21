my_number = input("Enter a number: ")
if my_number.isdigit():
    my_number = int(my_number)
    if my_number % 2 == 0:
        print("Even")
    else:
        print("Odd")

else:
    print(f''' {my_number} is not a number.
    Please enter a number''')
