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

# Ternary operator
#  The ternary operator is a shorthand way of writing an if statement
#  The syntax is:
number = 6
print("Even" if number % 2 == 0 else "Odd")
