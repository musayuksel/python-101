# Define and call your own functions
import random
import math
import calendar

from decimal import Decimal


def print_hi(name: str) -> None:
    print(f'Hi, {name}')


def square(number: int) -> int:
    return number ** 2


# print(f'The square of 4 is {square(4)}')

def multiply(number1: int, number2: int) -> int:
    return number1 * number2


print(calendar.month(2023, 5))  # print the calendar of May 2023

print(math.sqrt(4))  # print the square root of 4

# print a random number between 1 and 10 (inclusive)
print(random.randint(1, 10))

numbers = [12, 23, 45, 67, 65, 43]
print(random.choice(numbers))  # print a random number from the tuple
print(random.choice('computer'))  # print a random letter from the string
random.shuffle(numbers)  # shuffle the list
print(numbers)


print(round(8.92318, 4))  # 8.9232
print((1.2 - 1.0))  # weird result 0.19999999999999996
# Decimal is a class from the decimal module
# It is used for decimal floating point arithmetic
print(Decimal('1.2') - Decimal('1.0'))  # 0.2


int('10')  # 10
int('10', 2)  # 2 binary
int('1abc', 16)  # 6844 hexadecimal

# Boolean
bool(0)  # False
bool(1)  # True
bool('')  # False
bool([])  # False
bool({})  # False
bool(())  # False
bool(None)  # False
